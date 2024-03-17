from sys import stdout
from time import sleep

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from scrapper.models import Category, Topic, Book
from scrapper.serializer import CategorySerializer, TopicSerializer, BookSerializer


class CategoryListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.get_all_objects()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


class TopicListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.get_all_objects()
    serializer_class = TopicSerializer
    pagination_class = PageNumberPagination


class BookListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.get_all_objects()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination
