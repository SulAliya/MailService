from django.contrib import admin

from mails.models import Mails


@admin.register(Mails)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('newsletter', 'email',)
    list_filter = ('newsletter',)


