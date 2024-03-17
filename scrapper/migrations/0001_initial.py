# Generated by Django 5.0.3 on 2024-03-17 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('url_title', models.CharField(max_length=250, verbose_name='url_title')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('scrapped_at', models.DateTimeField(auto_now_add=True, verbose_name='scrapped_at')),
                ('books_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='book_num')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('url_title', models.CharField(max_length=250, verbose_name='url_title')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('scrapped_at', models.DateTimeField(auto_now_add=True, verbose_name='scrapped_at')),
                ('voters', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='voters')),
                ('books_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='book_num')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='scrapper.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'topic',
                'verbose_name_plural': 'topics',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('url_title', models.CharField(max_length=250, verbose_name='url_title')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('scrapped_at', models.DateTimeField(auto_now_add=True, verbose_name='scrapped_at')),
                ('voters', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='voters')),
                ('author', models.CharField(max_length=250, verbose_name='author')),
                ('rating', models.FloatField(blank=True, null=True, verbose_name='rating')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name='score')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_category', to='scrapper.category', verbose_name='category')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_topic', to='scrapper.topic', verbose_name='topic')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
    ]