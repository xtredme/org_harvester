# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser

# Добавляем поле с биографией 
# к стандартному набору полей (fieldsets) пользователя в админке.
UserAdmin.fieldsets += (
    # Добавляем кортеж, где первый элемент — это название раздела в админке,
    # а второй элемент — словарь, где под ключом fields можно указать нужные поля.
    ('Extra Fields', {'fields': (
                                 'surname',
                                 'job_title',
                                 'working_in_company',
                                 'superuser',
                                 'phone_number',
                                 'telegram_id',
                                 'telegram_name',
                                 'google_email',
                                 'work_email',
                                 'bio',
                                 'birthday',)}),
)
# Регистрируем модель в админке:
admin.site.register(MyUser, UserAdmin)