import os

from django.apps import AppConfig


class MailServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail_service'
    verbose_name = 'Сервис рассылки почты'

    def ready(self):
        if os.environ.get('RUN_MAIN') == 'True':
            from mail_service.services import start_scheduler
            start_scheduler()