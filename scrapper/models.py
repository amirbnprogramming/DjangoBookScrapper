from django.db import models
from abc import abstractmethod

from django.db.models import PositiveIntegerField


class BaseModel(models.Model):
    title = models.CharField(max_length=250, verbose_name='title')
    url_title = models.CharField(max_length=250, verbose_name='url_title')
    is_active = models.BooleanField(default=True, verbose_name='is_active')
    scrapped_at = models.DateTimeField(auto_now_add=True, verbose_name='scrapped_at')
    voters = PositiveIntegerField(default=None, verbose_name='voters', null=True, blank=True)
    books_number = models.PositiveIntegerField(verbose_name='book_num', null=True, blank=True)


    class Meta:
        abstract = True

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    def get_active_objects(cls):
        return cls.objects.filter(is_active=True).all()

    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()

    @classmethod
    def delete_all_objects(cls):
        cls.objects.all().delete()


class Category(BaseModel):
    voters = None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Topic(BaseModel):
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'topic'
        verbose_name_plural = 'topics'

    @classmethod
    def delete_objects_by_category(cls, category):
        cls.objects.filter(category=category).delete()


class Book(BaseModel):
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE, related_name='book_category')
    topic = models.ForeignKey(Topic, verbose_name='topic', on_delete=models.CASCADE, related_name='book_topic')
    author = models.CharField(max_length=250, verbose_name='author')
    rating = models.FloatField(verbose_name='rating', null=True, blank=True)
    score = models.IntegerField(verbose_name='score', null=True, blank=True)
    books_number = None


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
