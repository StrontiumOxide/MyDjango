# Generated by Django 5.0.3 on 2024-11-13 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основной')),
                ('articles', models.ManyToManyField(related_name='scopes', to='articles.article')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Имя')),
                ('scopes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='articles.scope')),
            ],
        ),
    ]