# from django.db import models


# class Article(models.Model):

#     title = models.CharField(max_length=256, verbose_name='Название')
#     text = models.TextField(verbose_name='Текст')
#     published_at = models.DateTimeField(verbose_name='Дата публикации')
#     image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
#     tags = models.ManyToManyField(to='Tag', related_name='articles', through='Scope')

#     class Meta:
#         verbose_name = 'Статья'
#         verbose_name_plural = 'Статьи'
#         ordering = ['-published_at']
#         unique_together = (('title', 'tags'),)

#     def __str__(self):
#         return self.title


# class Scope(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
#     tag = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='scopes')
#     is_main = models.BooleanField(verbose_name='Основной')


# class Tag(models.Model):

#     name = models.CharField(max_length=256, verbose_name='Имя')

#     def __str__(self):
#         return self.name
    

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    tags = models.ManyToManyField(to='Tag', related_name='articles', through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя', unique=True)

    def __str__(self):
        return self.name


class Scope(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        unique_together = (('article', 'tag'),) 
