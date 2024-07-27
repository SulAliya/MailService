from django.urls import path

from mails.apps import MailsConfig
from mails.views import MailsCreateView

app_name = MailsConfig.name

urlpatterns = [
    path('create/<int:pk>/', MailsCreateView.as_view(), name='create'),
]