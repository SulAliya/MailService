from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from mail_service.models import NewsLetter, Message


class LetterListView(ListView):
    model = NewsLetter


class LetterDetailView(DetailView):
    model = NewsLetter


class LetterCreateView(CreateView):
    model = NewsLetter
    fields = ('customer', 'message', 'date_and_time', 'frequency', 'status')
    success_url = reverse_lazy('mail_service:letter_list')


class LetterUpdateView(UpdateView):
    model = NewsLetter
    fields = ('customer', 'message', 'date_and_time', 'frequency', 'status')
    success_url = reverse_lazy('mail_service:letter_list')


class LetterDeleteView(DeleteView):
    model = NewsLetter
    success_url = reverse_lazy('mail_service:letter_list')


#crud для сообщения
class MessageListView(ListView):
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