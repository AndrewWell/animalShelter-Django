from django.db import models


class Cats(models.Model):
    title = models.CharField('Кличка кота', max_length=90)
    image = models.ImageField('Фотография кота', upload_to='main/static/main/img/cats')
    full_text = models.TextField('Информация о коте')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title


class Dogs(models.Model):
    title = models.CharField('Кличка собаки', max_length=90)
    image = models.ImageField('Фотография собаки', upload_to='main/static/main/img/dogs')
    full_text = models.TextField('Информация о собаке')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title


class Carousel(models.Model):
    title = models.CharField("Название картинки", max_length=30)
    image = models.ImageField("Фотография кошки/собаки", upload_to='main/static/main/img/carousel')
    date = models.DateField("Дата публикации")

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'Основной'
    verbose_name_plural = 'Основные'
