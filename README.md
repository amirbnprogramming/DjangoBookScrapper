
**Django Phonebook**

DjangoBookScrapper is a simple Django app to scrape goodreads website books .
Scrapped Data are categories , topics , and books ....
Application development and testing with django v4.2.4


Quick start
-----------

1. Set specific and custome settings for you project in ``local_settings.py``::
2. install packages in ``requirements.txt`` file with pip install -r
3. open terminal and  make migrations  for ``models`` ::

        python manage.py makemigrations     
        python manage.py migrate     

4.  Frist You should ``Scrape`` data and make objects for models and save in database ::

       python manage.py scrape --scrape    

5. After scraping data with commands instruction ``runserver`` and see the viewsets by urls ::

        python manage.py runserver

TODO
----

    - scrape data , save in database , then see the view
