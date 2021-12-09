from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(form=Post.news)
    queryset = queryset.order_by('-id')


class PostsDetail(DetailView):
    model = Post
    template_name = 'item.html'
    context_object_name = 'item'
    queryset = Post.objects.filter(form=Post.news)
