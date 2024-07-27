from django.db import models


class Mails(models.Model):
    newsletter = models.ForeignKey('mail_service.NewsLetter', on_delete=models.CASCADE, verbose_name='Рассылка')

    name = models.CharField(max_length=150, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email адрес')
    message = models.TextField()

    def __str__(self):
        return f'{self.newsletter} от {self.email}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
