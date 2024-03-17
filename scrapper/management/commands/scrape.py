import requests
import logging
from bs4 import BeautifulSoup
from django.core.management import BaseCommand

from scrapper.models import Category, Topic, Book

main_url = 'https://www.goodreads.com'

# Configure the logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


# region without celery
class Command(BaseCommand):
    help = 'Scrapes goodreads.com datas'

    def add_arguments(self, parser):
        parser.add_argument('--scrape', action='store_true', help='Run categories scrapper')

    def handle(self, *args, **options):
        if options['scrape']:
            self.scrape_category()

    def scrape_category(self):
        if Category.objects.exists():
            Category.delete_all_objects()
            print('All previous scrapped items deleted successfully.')

        url = main_url + '/list/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract category list information
        categories_block = soup.select('.listTagsTwoColumn > li')
        for category in categories_block:
            title_quantity = (category.text.split())
            title = title_quantity[0]
            quantity = int(title_quantity[1][1:-1])
            url_title = main_url + category.find('a').get('href')
            # object creating by scrapped data
            scrapped_category: Category = Category(title=title, books_number=quantity, url_title=url_title)
            scrapped_category.save()
            logging.info(f'scrapped category : {scrapped_category.title} - contains : ({scrapped_category.books_number}) books - {scrapped_category.url_title}')
            self.scrape_topic(url=url_title, category_parent=scrapped_category)

        self.stdout.write(self.style.SUCCESS('Scrapping Categories executed successfully.'))

    def scrape_topic(self, url, category_parent):
        logging.info(f'Starting scrapping Topics in ({category_parent.title}) Category . . .')
        if Topic.objects.filter(category=category_parent) is not None:
            Topic.delete_objects_by_category(category_parent)
            logging.info(f'Topics in category ({category_parent}) delete successfully.')

        url = url + '?page=1'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        cells = soup.select('.listRowsFull > .row > .cell')

        for item in cells:
            links = item.select_one('.listTitle')
            more_detail = item.select_one('.listFullDetails')
            title = links.text
            url_title = main_url + links.get('href')
            text = more_detail.text.replace("—", " ").replace(" ", "").split()
            books = ''.join([char for char in text[0] if char.isdigit()])
            voters = ''.join([char for char in text[1] if char.isdigit()])

            # object creating by scrapped data
            scrapped_topic: Topic = Topic(title=title, url_title=url_title,
                                          category=category_parent, books_number=books,
                                          voters=voters)
            scrapped_topic.save()
            logging.info(f'scrapped topic : {scrapped_topic.title} - contains : ({scrapped_topic.books_number}) books')

            self.scrape_book(url=url_title, topic_parent=scrapped_topic, category_parent=category_parent)

        self.stdout.write(
            self.style.SUCCESS(f'Topics in category ({category_parent.title}) , is scrapped successfully.'))

    def scrape_book(self, url, topic_parent, category_parent):
        logging.info(f'Starting scrapping books in ({topic_parent.title}) Topic')
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        td = soup.select('table > tr > td')
        for item in td:
            if item.get('width') == '100%':
                title_section = item.select_one('a.bookTitle')
                author_section = item.select_one('.authorName__container > a > span')
                rating_section = item.select_one('.minirating')
                score_section = item.select('div')[-1].find_all('a')

                url_title = main_url + title_section.get('href')
                title = title_section.select_one('span').text
                author = author_section.text
                avg_rating = rating_section.text.split('avg')[0].split()[-1]
                score = int(''.join([char for char in score_section[0].text if char.isdigit()]))
                voters = int(''.join([char for char in score_section[1].text if char.isdigit()]))

                # object creating by scrapped data
                scrapped_book: Book = Book(author=author, title=title, url_title=url_title,
                                           category=category_parent, topic=topic_parent,
                                           rating=avg_rating, score=score, voters=voters)
                scrapped_book.save()
                logging.info(
                    f'scrapped topic : {scrapped_book.title} - author : ({scrapped_book.author})')

        self.stdout.write(self.style.SUCCESS(f'Books in topic ({topic_parent.title}) , is scrapped successfully.'))

# endregion
