from django.shortcuts import render
from django.views.generic import ListView
from .models import Addresses, Order
from .forms import OrderForm


class PageView(ListView):
    template_name = 'main.html'
    queryset = ''


class PageView2(ListView):
    template_name = 'information.html'
    queryset = ''


class AddressesListView(ListView):
    model = Addresses
    template_name = 'addresses.html'
    context_object_name = 'addresses'
    queryset = Addresses.objects.all()
    queryset = queryset.order_by('-id')


class Orders(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'
    form_class = OrderForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)
