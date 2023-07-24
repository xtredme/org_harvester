from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    first_name = models.CharField('Имя', max_length=100, blank=True)
    last_name = models.CharField('Фамилия', max_length=100, blank=True)
    surname = models.CharField('Отчество', max_length=100, blank=True)
    job_title = models.CharField('Должность', max_length=100, blank=True)
    working_in_company = models.CharField('Место работы', max_length=100, blank=True)
    superuser = models.BooleanField('Суперпользователь', default=False)
    phone_number = models.CharField('Телефон', max_length=20, blank=True)
    telegram_id = models.CharField('Telegram ID', max_length=100, blank=True)
    telegram_name = models.CharField('Telegram имя', max_length=100, blank=True)
    google_email = models.EmailField('Google Email', blank=True)
    work_email = models.EmailField('Рабочий Email', blank=True)
    bio = models.TextField('Биография', blank=True)
    birthday = models.DateField('Дата рождения', blank=True, null=True)
    mega_admin_status = models.BooleanField('Мега Админ', default=False)

class Banlist(models.Model):
    banned_id = models.CharField('Забаненый Telegram ID', max_length=100, blank=True, null=True)
    ban_status = models.BooleanField('Статус бана', default=False, null=True)
    need_sorry = models.BooleanField('Нужно извиниться', default=False, null=True)
    created_at = models.DateTimeField('Время создания', auto_now_add=True, null=True)

