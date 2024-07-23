from django.urls import path
from mail_service.apps import MailServiceConfig
from mail_service.views import (LetterListView, LetterCreateView, LetterUpdateView, LetterDetailView, LetterDeleteView,
                                MessageCreateView, MessageUpdateView, MessageDeleteView, MessageListView,
                                MessageDetailView,
                                CustomerCreateView, CustomerListView, CustomerUpdateView, CustomerDeleteView,
                                CustomerDetailView)

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

    path('customer_list/', CustomerListView.as_view(), name='customer_list'),
    path('customer_service/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer_create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer_update/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer_delete/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

]

# urlpatterns = [
#     path('',  newsletters_list)
#     ]
