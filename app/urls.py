# coding: utf-8
from django.conf.urls import patterns, url

from django.views.generic import TemplateView
from app.views import PostsListView, PostDetailView
from app.models import Tag, Category

urlpatterns = patterns('',

url(r'^$', PostsListView.as_view(), name='list'),
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post'),
url(r'^news/$', PostsListView.as_view(), name='news'),
url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
url(r'^services/$', TemplateView.as_view(template_name='services.html'), name='services'),
url(r'^category/(?P<slug>[-\w]+)/$', 'app.views.category'),
url(r'^tag/(?P<slug>[-\w]+)/$', 'app.views.tag'),
)