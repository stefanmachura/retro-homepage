from django.db import models

class Entry(models.Model):
    author = models.CharField(max_length=200)
    pronouns = models.CharField(max_length=32, null=True)
    text = models.TextField(max_length=1000)
