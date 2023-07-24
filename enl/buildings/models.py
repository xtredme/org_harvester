from django.db import models



class Building(models.Model):
    title = models.CharField('Название объекта', max_length=128, null=True)
    brand = models.CharField('Бренд', max_length=128, blank=True, null=True)
    gas_number = models.IntegerField('Номер АЗС', blank=True, null=True, unique=True)
    start_date = models.DateField('Дата начала строительства', blank=True, null=True)
    finish_date = models.DateField('Дата окончания строительства', blank=True, null=True)
    warranty_start_date = models.DateField('Дата начала гарантии', blank=True, null=True)
    warranty_time = models.IntegerField('Количество лет гарантии', blank=True, null=True)
    executor = models.CharField('Исполнитель (Подрядчик)', max_length=128, null=True)
    phone_executor = models.CharField('Номер исполнителя', max_length=20, blank=True, null=True, unique=True)
    warranty = models.BooleanField('Статус гарантии 2 года', default=False, null=True)
    curator = models.CharField('Куратор от ВДС', max_length=128, null=True)


test = 'Hello'