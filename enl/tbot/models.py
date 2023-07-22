from django.db import models

class Tbot(models.Model):
    title = models.CharField(max_length=128)