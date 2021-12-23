# from django.views.generic import ListView, DetailView
# from .models import Product
# import datetime
#
#
# class ProductsList(ListView):
#     model = Product  # указываем модель, объекты которой мы будем выводить
#     template_name = 'products.html'  # указываем имя шаблона, где будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
#     context_object_name = 'products'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
#     queryset = Product.objects.order_by('-id')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['time_now'] = datetime.datetime.utcnow()  # добавим переменную текущей даты time_now
#         context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
#         return context
#
#
# # создаём представление, в котором будут детали конкретного отдельного товара
# class ProductDetail(DetailView):
#     model = Product  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
#     template_name = 'product.html'  # название шаблона будет product.html
#     context_object_name = 'product'  # название объекта. в нём будет

from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView # импортируем необходимые дженерики

from django.core.paginator import Paginator

from .models import Product, Category
from .filters import ProductFilter
from .forms import ProductForm


# из списка на главной странице уберём всё лишнее
class Products(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context


# дженерик для получения деталей о товаре
class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm


# дженерик для редактирования объекта
class ProductUpdateView(UpdateView):
    template_name = 'product_create.html'
    form_class = ProductForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)


# дженерик для удаления товара
class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'
