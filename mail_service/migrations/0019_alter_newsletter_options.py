# Generated by Django 5.0.7 on 2024-08-02 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_service', '0018_alter_attempt_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'permissions': [('can_delete_newsletter', 'Can delete newsletter'), ('can_view_newsletter', 'Can view newsletter'), ('can_delete_client', 'Can delete client'), ('can_view_client', 'Can view client')], 'verbose_name': 'Рассылка (настройки)', 'verbose_name_plural': 'Рассылки (настройки)'},
        ),
    ]
