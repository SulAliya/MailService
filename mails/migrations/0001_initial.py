# Generated by Django 5.0.7 on 2024-07-24 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mail_service', '0008_attempt_mailing_parameters_newsletter_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('email', models.EmailField(max_length=254, verbose_name='Email адрес')),
                ('message', models.TextField()),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail_service.newsletter', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]
