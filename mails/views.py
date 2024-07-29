from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from mails.models import Mails
from mails.services import send_mailing


class MailsCreateView(CreateView):
    model = Mails
    fields = ('name', 'email', 'message',)

    def get_success_url(self):
        return reverse('mail_service:mails_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['newsletter'] = get_object_or_404(Mails, pk=self.kwargs.get('pk'))
        return context_data

    def form_valid(self, form):
        obj = form.save()
        send_mailing(obj)
        return super().form_valid(form)
