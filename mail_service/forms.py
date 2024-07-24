from django.forms import ModelForm

from mail_service.models import NewsLetter, Message, Customer


class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
