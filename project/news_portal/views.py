from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from .models import Post, Category, Subscribers
from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView
from .filters import NewsFilter
from django.core.paginator import Paginator
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django import template
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Post, Subscribers, User


class PostsListView(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.all()
    queryset = queryset.order_by('-id')


class PostDetailView(DetailView):
    model = Post
    template_name = 'item.html'
    context_object_name = 'item'
    queryset = Post.objects.all()


class PostAddView(PermissionRequiredMixin, CreateView):
    permission_required = ('news_portal.add_post',)
    model = Post
    template_name = 'post_add_edit.html'
    context_object_name = 'item'
    queryset = Post.objects.all()
    form_class = PostForm
    success_url = '/news/search/'


class PostEditView(PermissionRequiredMixin, UpdateView):
    permission_required = ('news_portal.change_post',)
    model = Post
    template_name = 'post_add_edit.html'
    context_object_name = 'item'
    queryset = Post.objects.all()
    form_class = PostForm
    success_url = '/news/search/'


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('news_portal.delete_post',)
    template_name = 'post_delete.html'
    context_object_name = 'item'
    queryset = Post.objects.all()
    success_url = '/news/search/'


# @method_decorator(login_required, name='dispatch')
class PostsSearchListView(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = '-publication_date_and_time'
    queryset = Post.objects.all()
    # queryset = Post.objects.filter(form=Post.news)
    paginate_by = 10
    form_class = PostForm

    def get_context_data(self, **kwargs):
        # print(self.request.GET)
        context = super().get_context_data(**kwargs)
        # print(context)
        filtered = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = filtered

        paginated_filtered_persons = Paginator(filtered.qs, self.paginate_by)
        page_number = self.request.GET.get('page')
        person_page_object = paginated_filtered_persons.get_page(page_number)
        context['person_page_object'] = person_page_object

        context['categories'] = Category.objects.all()
        context['form'] = PostForm()

        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем
            form.save()

        return super().get(request, *args, **kwargs)


# def subscribe_me(request):
    # user = request.user
    # post_category = Category.objects.filter(id=id)[0]
    # if Subscribers.objects.filter(user_id=user.id, category_id=post_category.id).exists():
    #     response = HttpResponse()
    #     response.write(f"<p>Вы уже подписаны на новости в категории {post_category.name}</p>")
    #     response.write('<a class="nav-link" href="/news/search/">Вернуться</a>')
    #     return response
    # else:
    #     Subscribers.objects.create(user_id=user.id, category_id=post_category.id)
    #     response = HttpResponse()
    #     response.write(f"<p>Вы подписались на новости в категории {post_category.name}</p>")
    #     response.write('<a class="nav-link" href="/news/search/">Вернуться</a>')
    #     return response
