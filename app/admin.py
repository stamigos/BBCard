__author__ = 'Amigos'

from django.contrib import admin
from app.models import Post
from app.models import Tag, Category

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)