from django.contrib import admin

from mail_service.models import Message, Customer, NewsLetter, Attempt


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment',)
    list_filter = ('name', 'email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('letter_subject', 'body',)


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('date_and_time', 'frequency', 'status',)
    list_filter = ('status',)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('date_and_time', 'is_success', 'answer',)
    list_filter = ('is_success',)



