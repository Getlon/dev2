from django.urls import path
from .views import PostDetail, PostsList, PostsSearchList

app_name = 'news_portal'
urlpatterns = [
    path('', PostsList.as_view()),
    path('search/', PostsSearchList.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='item'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
]
