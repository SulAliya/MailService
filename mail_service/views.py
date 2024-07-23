from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from mail_service.models import NewsLetter, Message, Customer


class LetterListView(ListView):
    model = NewsLetter


class LetterDetailView(DetailView):
    model = NewsLetter


class LetterCreateView(CreateView):
    model = NewsLetter
    fields = ('name', 'customer', 'message', 'date_and_time', 'frequency', 'status')
    success_url = reverse_lazy('mail_service:letter_list')


class LetterUpdateView(UpdateView):
    model = NewsLetter
    fields = ('name', 'customer', 'message', 'date_and_time', 'frequency', 'status')
    success_url = reverse_lazy('mail_service:letter_list')


class LetterDeleteView(DeleteView):
    model = NewsLetter
    success_url = reverse_lazy('mail_service:letter_list')


#crud для сообщения
class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ('letter_subject', 'body')
    success_url = reverse_lazy('mail_service:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('letter_subject', 'body')
    success_url = reverse_lazy('mail_service:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mail_service:message_list')


#crud для клиента
class CustomerListView(ListView):
    model = Customer


class CustomerDetailView(DetailView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('mail_service:customer_list')


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('mail_service:customer_list')


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('mail_service:customer_list')