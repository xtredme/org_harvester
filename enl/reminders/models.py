from django.db import models

class Reminder(models.Model):
    name_reminder = models.CharField('Название напоминания', max_length=100, blank=True, null=True)
    text_reminder = models.CharField('Текст напоминания', blank=True, null=True)
    reminder_interval = models.IntegerField('Интервал напоминания в минутах', blank=True, null=True)
    status_reminder = models.BooleanField('Статус активности напоминания', blank=True, null=True)
    created_at = models.DateTimeField('Время создания', auto_now_add=True, null=True)
    owner_reminder_id = models.IntegerField('телеграм id создателя', blank=True, null=True)
    reminder_chat_id = models.IntegerField('чат id создания напоминания', blank=True, null=True)
    reminder_last_view_time = models.DateTimeField('Время последнего показа', blank=True, null=True)
    next_reminder_time = models.DateTimeField('Время следующего показа', blank=True, null=True)

    def __str__(self):
        return self.name_reminder
