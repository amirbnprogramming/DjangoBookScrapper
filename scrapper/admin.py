from django.contrib import admin
from scrapper.models import Category, Topic, Book


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'books_number', 'is_active', 'scrapped_at']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'books_number', 'is_active', 'voters', 'scrapped_at']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'topic', 'title', 'author', 'rating', 'score', 'scrapped_at', 'voters']
