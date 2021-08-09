from django.db import models

class Entry(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
