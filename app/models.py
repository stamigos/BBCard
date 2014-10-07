# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, editable=False)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, editable=False)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Дата публикации')
    content = models.TextField(max_length=10000)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%i/" % self.id