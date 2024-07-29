# import smtplib
#
# import pytz
# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime, timedelta
#
# from django.conf import settings
#
# from django.core.mail import send_mail
# from django.utils import timezone
#
# from mail_service.models import NewsLetter, Attempt
#
#
# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(send_mailing, 'interval', seconds=60)
#     scheduler.start()
#
#
# # Главная функция по отправке рассылки
# def send_mailing():
#     zone = pytz.timezone(settings.TIME_ZONE)
#     current_datetime = datetime.now(zone)
#     # создание объекта с применением фильтра
#     mailings = (
#         NewsLetter.objects.filter(date_and_time__lte=current_datetime).filter(status__in=['STARTED']))
#
#     for mailing in mailings:
#
#         rl = [customer.email for customer in mailing.customer.all()]
#         server_response = ''
#         status = False
#         try:
#             server_response = send_mail(
#                 subject=mailing.mail.theme,
#                 message=mailing.mail.content,
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=rl,
#                 fail_silently=False
#             )
#             server_response = str(server_response)
#             status = True
#         except smtplib.SMTPException as e:
#             server_response = str(e)
#             status = False
#         finally:
#             log = Attempt(is_success=status, answer=server_response, date_and_time=current_datetime,
#                           mailing_parameters=mailing)
#             print(log)
#             log.save()
#
#             next_date_calculated = None
#             # получаем следующий расчетный день рассылки
#             if mailing.interval == 'per_day':
#                 next_date_calculated = mailing.next_date + timezone.timedelta(days=1)
#             elif mailing.interval == 'per_week':
#                 next_date_calculated = mailing.next_date + timezone.timedelta(days=7)
#             elif mailing.interval == 'per_month':
#                 next_date_calculated = mailing.next_date + timezone.timedelta(days=30)
#
#             if next_date_calculated > mailing.end_time:
#                 if status:
#                     mailing.status = 'finished'
#                 else:
#                     mailing.status = 'finished_error'
#             else:
#                 mailing.next_date = next_date_calculated
#
#             mailing.save()
import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.mail import send_mail

from mail_service.models import NewsLetter, Message, Attempt
from apscheduler.schedulers.background import BackgroundScheduler


def send_newsletter_email(objects):
    try:
        message_instance = Message.objects.first()  # Замени на подходящий запрос
        server_response = send_mail(
            subject=message_instance.letter_subject,
            message=message_instance.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email for client in objects.client.all()],
            fail_silently=False,
        )
        log = Attempt.objects.create(mailing_parameters=objects, answer=server_response)
        if server_response:
            log.status = 'Успешно'
            log.save()
        if objects.status == 'создана':
            objects.status = 'запущена'
            objects.save()
    except smtplib.SMTPException as e:
        log=Attempt.objects.create(mailing_parameters=objects, answer=e)
        log.save()


def send_newsletter_periodic_email():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    print(f'дата - {current_datetime}')

    for obj in NewsLetter.objects.filter(status__in=('создана', 'запущена')):
        if obj.start_time < current_datetime < obj.end_time:

            log = Attempt.objects.filter(newsletter=obj)
            print(f'первый - {log}')
            if log.exists():
                last_log = log.order_by('time').last()
                current_timedelta = current_datetime - last_log.time
                print(current_timedelta)

                if obj.periodicity == 'day' and current_timedelta <= timedelta(days=1):
                    send_newsletter_email(obj)
                    print(f'раз в день')
                elif obj.periodicity == 'week' and current_timedelta >= timedelta(weeks=1):
                    send_newsletter_email(obj)
                    print(f'раз в неделю')
                elif obj.periodicity == 'month' and current_timedelta >= timedelta(
                        weeks=4):
                    send_newsletter_email(obj)
                    print(f'раз в месяц')
                elif obj.periodicity == 'minute' and current_timedelta >= timedelta(minutes=1):
                    send_newsletter_email(obj)
                    print(f'раз в minute')
            else:
                send_newsletter_email(obj)
                print(f'иначе')
        elif current_datetime > obj.end_time:
            obj.status = 'завершена'
            obj.save()


def start_scheduler():
    scheduler = BackgroundScheduler()

    # Проверка, добавлена ли задача уже
    if not scheduler.get_jobs():
        scheduler.add_job(send_newsletter_periodic_email, 'interval', seconds=30)

    if not scheduler.running:
        scheduler.start()