# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    ct_slug = models.CharField(max_length=100, editable=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/%i/" % self.id


class Tag(models.Model):
    name = models.CharField(max_length=50)
    tg_slug = models.CharField(max_length=50, editable=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/%i/" % self.id


class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    datetime = models.DateTimeField(u'Дата публикации')
    content = RichTextField()
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%i/" % self.id