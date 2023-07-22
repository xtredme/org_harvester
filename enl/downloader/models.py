from django.db import models

class Downloader(models.Model):
    title = models.CharField(max_length=128)