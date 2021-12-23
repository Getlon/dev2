from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Category
from django.views.generic import ListView
from .filters import NewsFilter
from django.core.paginator import Paginator
from .forms import PostForm


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


class PostAddView(CreateView):
    model = Post
    template_name = 'post_add_edit.html'
    context_object_name = 'item'
    queryset = Post.objects.all()
    form_class = PostForm
    success_url = '/news/search/'


class PostEditView(UpdateView):
    model = Post
    template_name = 'post_add_edit.html'
    context_object_name = 'item'
    queryset = Post.objects.all()
    form_class = PostForm
    success_url = '/news/search/'


class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    context_object_name = 'item'
    queryset = Post.objects.all()
    success_url = '/news/search/'


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
