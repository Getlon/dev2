from django.urls import path
from .views import Products, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView

urlpatterns = [
    path('', Products.as_view()),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # product_detail
    # Ссылка на детали товара
    path('create/', ProductCreateView.as_view(), name='product_create'),
    # Ссылка на создание товара
    path('create/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]

