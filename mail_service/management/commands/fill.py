from django.core.management import BaseCommand

from mail_service.services import start


class Command(BaseCommand):
    """Команда на запуск рассылки"""

    def handle(self, *args, **options):

        start()
