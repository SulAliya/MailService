from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from mail_service.forms import NewsLetterForm, MessageForm, ClientForm
from mail_service.models import NewsLetter, Message, Client


class LetterListView(ListView):
    model = NewsLetter


class LetterDetailView(DetailView):
    model = NewsLetter


class LetterCreateView(CreateView):
    model = NewsLetter
    form_class = NewsLetterForm
    success_url = reverse_lazy('mail_service:letter_list')


class LetterUpdateView(UpdateView):
    model = NewsLetter
    form_class = NewsLetterForm
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
    form_class = MessageForm
    success_url = reverse_lazy('mail_service:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail_service:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mail_service:message_list')


#crud для клиента
class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail_service:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail_service:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mail_service:client_list')