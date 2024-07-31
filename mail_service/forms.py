from django.forms import ModelForm

from mail_service.models import NewsLetter, Message, Client


class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'


class NewsLetterModeratorForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
