# Generated by Django 5.0.3 on 2024-10-26 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name'], 'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['name'], 'verbose_name': 'Учитель', 'verbose_name_plural': 'Учителя'},
        ),
    ]