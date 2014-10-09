# coding: utf-8
from django.conf.urls import patterns, url

from django.views.generic import TemplateView
from app.views import PostsListView, PostDetailView

urlpatterns = patterns('',

#url(r'^$', PostsListView.as_view(), name='list'),
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post'),
url(r'^news/$', PostsListView.as_view(), name='news'),
url(r'^$', TemplateView.as_view(template_name='about.html'), name='about'),
url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
url(r'^services/$', TemplateView.as_view(template_name='services.html'), name='services'),
url(r'^(\d+)/category/(?P<id>\d+)/$', 'app.views.category'),
url(r'^(\d+)/tag/(?P<id>\d+)/$', 'app.views.tag'),
)