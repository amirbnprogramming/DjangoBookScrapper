from django.urls import path, include
from rest_framework.routers import DefaultRouter

from scrapper import views

category_router = DefaultRouter()
topic_router = DefaultRouter()
book_router = DefaultRouter()

category_router.register('', views.CategoryListViewSet, basename='category_list')
topic_router.register('', views.TopicListViewSet, basename='topic_list')
book_router.register('', views.BookListViewSet, basename='book_list')

urlpatterns = [
    path('category/', include(category_router.urls)),
    path('topic/', include(topic_router.urls)),
    path('books/', include(book_router.urls)),
]
