# Generated by Django 4.2.6 on 2023-10-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('image', models.ImageField(upload_to='news/static/img/articles', verbose_name='Картинка к статье')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='PrepositionalNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('image', models.ImageField(upload_to='news/static/img/prepositionalNews', verbose_name='Картинка к статье')),
                ('full_text', models.TextField(verbose_name='Статья')),
            ],
        ),
    ]
