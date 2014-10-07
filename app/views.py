# Create your views here.
from pytils import translit

from app.models import Post, Category, Tag
from django.views.generic import ListView, DetailView
from django.shortcuts import render


def category(request, id):
    category = Category.objects.select_related().get(id=id)
    posts = category.post_set.all()
    slug = translit.slugify(category.name)
    return render(request, 'category.html', {'posts': posts,
                                            'category': category, 'slug': slug})

def tag (request, id):
    tag = Tag.objects.select_related().get(id=id)
    posts = tag.post_set.all()
    slug = translit.slugify(tag.name)
    return render(request, 'tagpage.html', {'posts': posts,
                                            'tag': tag,
                                            'slug': slug})

class PostsListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post