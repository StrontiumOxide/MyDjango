from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):

    is_main = models.BooleanField(verbose_name='Основной')
    articles = models.ManyToManyField(to='Article', related_name='scopes')


class Tag(models.Model):

    name = models.CharField(max_length=256, verbose_name='Имя')
    scopes = models.ForeignKey(to='Scope', on_delete=models.CASCADE, related_name='tag')

    def __str__(self):
        return self.name
    