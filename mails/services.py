import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime, timedelta
from config.settings import EMAIL_HOST_USER
from mail_service.models import Attempt, NewsLetter


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, 'interval', seconds=60)
    scheduler.start()


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = NewsLetter.objects.filter(date_and_time__lte=current_datetime).filter(
        status__in=['Создана', 'Запущена', 'Завершена'])

    for mailing in mailings:
        send_mail(
            subject=theme,
            message=text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email for client in mailing.customer.all()]
        )

    # try:
    #     server_response = send_mail(
    #         f'{obj.message.subject}',
    #         f'{obj.message.text}',
    #         EMAIL_HOST_USER,
    #         recipient_list=[customer.email for customer in obj.customer.all()],
    #         fail_silently=False,
    #     )
    #     a = Attempt.objects.create(newletter=obj, server_response=server_response)
    #     if server_response:
    #         a.is_success = True
    #     a.save()
    # except smtplib.SMTPException:
    #     Attempt.objects.create(newletter=obj, server_response=0)
    # if obj.status == 'Создана':
    #     obj.status = 'Запущена'
    #     obj.save()
