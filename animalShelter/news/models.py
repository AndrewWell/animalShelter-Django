from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=90)
    anons = models.CharField('Анонс', max_length=250)
    image = models.ImageField('Картинка к статье', upload_to='news/static/img/articles')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.anons

class PrepositionalNews(models.Model):
    title = models.CharField('Название', max_length=90)
    anons = models.CharField('Анонс', max_length=250)
    image = models.ImageField('Картинка к статье', upload_to='news/static/img/prepositionalNews')
    full_text = models.TextField('Статья')


class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'
