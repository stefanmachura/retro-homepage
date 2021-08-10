from django.db import models


class SiteStats(models.Model):
    counter = models.IntegerField(default=0)
