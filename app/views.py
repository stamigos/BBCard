# Create your views here.
from app.models import Post, Category, Tag
from django.views.generic import ListView, DetailView

from django.shortcuts import render


def category(request, id):
    category = Category.objects.select_related().get(id=id)
    posts = category.post_set.all()
    return render(request, 'category.html', {'posts': posts,
                                            'category': category})

def tag (request, id):
    tag = Tag.objects.select_related().get(id=id)
    posts = tag.post_set.all()
    return render(request, 'tagpage.html', {'posts': posts, 'tag': tag})

class PostsListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post