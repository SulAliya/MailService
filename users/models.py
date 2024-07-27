from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField('Email address', unique=True)
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='аватар', blank=True, null=True,
                               help_text='Загрузите свой аватар')
    phone = models.CharField(max_length=35, verbose_name='номер телефона', blank=True, null=True,
                             help_text='Введите номер телефона')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
