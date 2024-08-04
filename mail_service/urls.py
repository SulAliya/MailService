from django.urls import path
from django.views.decorators.cache import cache_page

from mail_service.apps import MailServiceConfig
from mail_service.views import (LetterListView, LetterCreateView, LetterUpdateView, LetterDetailView, LetterDeleteView,
                                MessageCreateView, MessageUpdateView, MessageDeleteView, MessageListView,
                                MessageDetailView,
                                ClientCreateView, ClientListView, ClientUpdateView, ClientDeleteView,
                                ClientDetailView)

app_name = MailServiceConfig.name

urlpatterns = [
    path('', LetterListView.as_view(), name='letter_list'),
    path('mail_service/<int:pk>/', LetterDetailView.as_view(), name='letter_detail'),
    path('mail_service/create', LetterCreateView.as_view(), name='letter_create'),
    path('mail_service/<int:pk>/update/', LetterUpdateView.as_view(), name='letter_update'),
    path('mail_service/<int:pk>/delete/', LetterDeleteView.as_view(), name='letter_delete'),

    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_service/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_update/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_service/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

]

# urlpatterns = [
#     path('',  newsletters_list)
#     ]
