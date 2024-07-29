from django.core.management import BaseCommand

from mail_service.services import send_newsletter_periodic_email


class Command(BaseCommand):
    """Команда на запуск рассылки"""

    def handle(self, *args, **options):

        send_newsletter_periodic_email()
