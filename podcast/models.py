from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Episode(models.Model):
    number = models.IntegerField()
    date = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    pod_link = models.CharField(max_length=50)
    img_link = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title