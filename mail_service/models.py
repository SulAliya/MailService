from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):  # Клиент сервиса.
    name = models.CharField(max_length=100, verbose_name='Ф.И.О.')
    email = (models.EmailField(max_length=100, verbose_name='Контактный email', unique=True))
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.email} \n {self.comment}'

    class Meta:
        verbose_name = 'Клиент сервиса'
        verbose_name_plural = 'Клиенты сервиса'


class Message(models.Model):  # Сообщение для рассылки.
    letter_subject = models.TextField(verbose_name='тема письма', **NULLABLE)
    body = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return f'Тема письма: {self.letter_subject}. \n Сообщение: {self.body}'

    class Meta:
        verbose_name = 'Сообщение для рассылки'
        verbose_name_plural = 'Сообщения для рассылки'


class NewsLetter(models.Model):  # Рассылка (настройки).
    CREATED = 'Создана'
    STARTED = 'Запущена'
    FINISHED = 'Завершена'
    MINUTLY = 'minutly'
    DAILY = 'daily',
    WEEKLY = 'weekly',
    MONTHLY = 'monthly',

    STATUS_CHOICES = (
        ('CREATED', 'Создана'),
        ('STARTED', 'Запущена'),
        ('FINISHED', 'Завершена'),
    )

    FREQUENCY_CHOICES = (
        ('MINUTLY', 'раз в минуту'),
        ('DAILY', 'раз в день'),
        ('WEEKLY', 'раз в неделю'),
        ('MONTHLY', 'раз в месяц'),
    )
    name = models.CharField(max_length=50, verbose_name='Название рассылки', default='без названия', **NULLABLE)
    client = models.ManyToManyField(Client, verbose_name='Клиент сервиса', help_text='Укажите клиентов')
    message = models.ForeignKey(Message, verbose_name='Сообщение', on_delete=models.CASCADE, **NULLABLE)
    start_time = models.DateTimeField(verbose_name='время начала рассылки', **NULLABLE)
    end_time = models.DateTimeField(verbose_name='время окончания рассылки', **NULLABLE)
    frequency = models.CharField(verbose_name='Периодичность: раз в день, раз в неделю, раз в месяц',
                                 choices=FREQUENCY_CHOICES,
                                 default=DAILY  # По умолчанию раз в день.
                                 )
    status = models.CharField(verbose_name='Статус рассылки (например, завершена, создана, запущена)',
                              default=CREATED,  # По умолчанию создана.
                              choices=STATUS_CHOICES
                              )

    def __str__(self):
        return f'{self.start_time} /n {self.frequency} /n {self.status}'

    class Meta:
        verbose_name = 'Рассылка (настройки)'
        verbose_name_plural = 'Рассылки (настройки)'
        permissions = [
            ('can_delete_newsletter', "Can delete newsletter"),
            ('can_view_newsletter', "Can view newsletter"),
            ('can_delete_user', "Can delete user"),
            ('can_view_user', "Can view user")
        ]


class Attempt(models.Model):  # Попытка рассылки.
    LOG_SUCCESS = 'Успешно'
    LOG_FAIL = 'Неуспешно'

    STATUS_VARIANTS = [
        (LOG_SUCCESS, 'Успешно'),
        (LOG_FAIL, 'Неуспешно'),
    ]

    mailing_parameters = models.ForeignKey(NewsLetter, on_delete=models.CASCADE,
                                           verbose_name='параметры рассылки', **NULLABLE)
    time = models.DateTimeField(verbose_name='дата и время последней попытки', auto_now_add=True)
    status = models.CharField(verbose_name='статус попытки (успешно / не успешно)', choices=STATUS_VARIANTS)
    server_response = models.CharField(verbose_name='ответ почтового сервера, если он был')

    def __str__(self):
        return f'{self.time} /n {self.status} /n {self.server_response}'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
