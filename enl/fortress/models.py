from django.db import models

class Fortress(models.Model):
    title = models.CharField(max_length=128)