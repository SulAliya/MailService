import smtplib

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

from django.conf import settings

from django.core.mail import send_mail
from django.utils import timezone

from mail_service.models import NewsLetter, Attempt


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, 'interval', seconds=60)
    scheduler.start()


# Главная функция по отправке рассылки
def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = (
        NewsLetter.objects.filter(date_and_time__lte=current_datetime).filter(status__in=['STARTED']))

    for mailing in mailings:

        rl = [customer.email for customer in mailing.customer.all()]
        server_response = ''
        status = False
        try:
            server_response = send_mail(
                subject=mailing.mail.theme,
                message=mailing.mail.content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=rl,
                fail_silently=False
            )
            server_response = str(server_response)
            status = True
        except smtplib.SMTPException as e:
            server_response = str(e)
            status = False
        finally:
            log = Attempt(is_success=status, answer=server_response, date_and_time=current_datetime,
                          mailing_parameters=mailing)
            print(log)
            log.save()

            next_date_calculated = None
            # получаем следующий расчетный день рассылки
            if mailing.interval == 'per_day':
                next_date_calculated = mailing.next_date + timezone.timedelta(days=1)
            elif mailing.interval == 'per_week':
                next_date_calculated = mailing.next_date + timezone.timedelta(days=7)
            elif mailing.interval == 'per_month':
                next_date_calculated = mailing.next_date + timezone.timedelta(days=30)

            if next_date_calculated > mailing.end_time:
                if status:
                    mailing.status = 'finished'
                else:
                    mailing.status = 'finished_error'
            else:
                mailing.next_date = next_date_calculated

            mailing.save()
