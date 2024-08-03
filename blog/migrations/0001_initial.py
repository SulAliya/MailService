# Generated by Django 4.2.2 on 2024-08-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=100, null=True, verbose_name='Slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержимое статьи')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/preview', verbose_name='изображение')),
                ('created_at', models.DateField(blank=True, null=True, verbose_name='дата публикации')),
                ('number_of_views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
