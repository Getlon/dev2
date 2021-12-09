from .views import ProductsList, ProductDetail
from django.urls import path

urlpatterns = [
    path('', ProductsList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
]
