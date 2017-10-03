from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class Abou(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0) # Record how often a post is seen
    tag = models.CharField(max_length=30, blank=True, null=True)
    latitude = models.CharField(max_length=25, blank=True, null=True)
    longitude = models.CharField(max_length=25, blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to='images')
    vr_image = models.ImageField(upload_to='images')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title