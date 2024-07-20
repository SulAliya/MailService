# Generated by Django 5.0.6 on 2024-06-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ф.И.О.')),
                ('email', models.CharField(max_length=100, verbose_name='Контактный email')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент сервиса',
                'verbose_name_plural': 'Клиенты сервиса',
            },
        ),
        migrations.DeleteModel(
            name='MailService',
        ),
    ]
