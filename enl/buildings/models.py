from django.db import models

class Building(models.Model):
    title = models.CharField(max_length=128)