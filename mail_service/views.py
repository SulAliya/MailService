from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from mail_service.forms import NewsLetterForm, MessageForm, ClientForm, NewsLetterModeratorForm
from mail_service.models import NewsLetter, Message, Client


class LetterListView(ListView):
    model = NewsLetter


class LetterDetailView(DetailView):
    model = NewsLetter


class LetterCreateView(CreateView, LoginRequiredMixin):
    model = NewsLetter
    form_class = NewsLetterForm
    success_url = reverse_lazy('mail_service:letter_list')

    def form_valid(self, form):
        letter = form.save()
        user = self.request.user
        letter.owner = user
        letter.save()
        return super().form_valid(form)


class LetterUpdateView(LoginRequiredMixin, UpdateView):
    model = NewsLetter
    form_class = NewsLetterForm
    success_url = reverse_lazy('mail_service:letter_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return NewsLetterForm
        if (user.has_perm('mail_service.can_delete_newsletter') and user.has_perm(
                'mail_service.can_view_newsletter')):
            return NewsLetterModeratorForm
        raise PermissionDenied


class LetterDeleteView(DeleteView):
    model = NewsLetter
    success_url = reverse_lazy('mail_service:letter_list')


# crud для сообщения
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

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return NewsLetterForm
        if (user.has_perm('mail_service.can_delete_newsletter') and user.has_perm(
                'mail_service.can_view_newsletter') and user.has_perm('mail_service.can_delete_client')
                and user.has_perm('mail_service.can_view_client')):
            return NewsLetterModeratorForm
        raise PermissionDenied


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mail_service:message_list')


# crud для клиента
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

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return NewsLetterForm
        if (user.has_perm('mail_service.can_delete_newsletter') and user.has_perm(
                'mail_service.can_view_newsletter') and user.has_perm('mail_service.can_delete_client')
                and user.has_perm('mail_service.can_view_client')):
            return NewsLetterModeratorForm
        raise PermissionDenied


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mail_service:client_list')
