from django.urls import path
from .views import PostsDetail, PostsList

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostsDetail.as_view()),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
]
