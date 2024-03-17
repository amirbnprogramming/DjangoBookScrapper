from rest_framework import serializers

from scrapper.models import Category, Topic, Book


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
