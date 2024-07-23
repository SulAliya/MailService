from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Customer(models.Model):  # Клиент сервиса.
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
    DAILY = 'daily',
    WEEKLY = 'weekly',
    MONTHLY = 'monthly',

    STATUS_CHOICES = (
        ('Создана', 'Создана'),
        ('Запущена', 'Запущена'),
        ('Завершена', 'Завершена'),
    )

    FREQUENCY_CHOICES = (
        ('Раз в день', 'раз в день'),
        ('Раз в неделю', 'раз в неделю'),
        ('Раз в месяц', 'раз в месяц'),
    )
    name = models.CharField(max_length=50, verbose_name='Название рассылки', default='без названия', **NULLABLE)
    customer = models.ManyToManyField(Customer, verbose_name='Клиент сервиса', help_text='Укажите клиентов')
    message = models.OneToOneField(Message, verbose_name='Сообщение', on_delete=models.CASCADE, **NULLABLE)

    date_and_time = models.DateTimeField(verbose_name='Дата и время первой отправки рассылки(дд.мм.гг)')
    frequency = models.CharField(verbose_name='Периодичность: раз в день, раз в неделю, раз в месяц',
                                 choices=FREQUENCY_CHOICES,
                                 default=DAILY  # По умолчанию раз в день.
                                 )
    status = models.CharField(verbose_name='Статус рассылки (например, завершена, создана, запущена)',
                              default=CREATED,  # По умолчанию создана.
                              choices=STATUS_CHOICES
                              )

    def __str__(self):
        return f'{self.date_and_time} /n {self.frequency} /n {self.status}'

    class Meta:
        verbose_name = 'Рассылка (настройки)'
        verbose_name_plural = 'Рассылки (настройки)'


class Attempt(models.Model):  # Попытка рассылки.
    mailing_parameters = models.ForeignKey(NewsLetter, on_delete=models.CASCADE,
                                           verbose_name='параметры рассылки', **NULLABLE)
    date_and_time = models.DateTimeField(verbose_name='дата и время последней попытки')
    status = models.CharField(verbose_name='статус попытки (успешно / не успешно)')
    answer = models.TextField(verbose_name='ответ почтового сервера, если он был')

    def __str__(self):
        return f'{self.date_and_time} /n {self.status} /n {self.answer}'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
