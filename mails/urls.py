from django.urls import path

from mails.apps import MailsConfig
from mails.views import MailsCreateView

app_name = MailsConfig.name

urlpatterns = [
    path('mails/create', MailsCreateView.as_view(), name='mails_create'),

]