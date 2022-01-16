from django.urls import path, include
from .views import PostDetailView, PostsListView, PostsSearchListView, PostAddView, PostEditView, PostDeleteView
from .templatetags.custom_simple_tag import subscribe_me1, subscribe_me2, subscribe_me3, subscribe_me4


urlpatterns = [
    path('', PostsListView.as_view()),
    path('search/', PostsSearchListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('add/', PostAddView.as_view(), name='post_add'),
    path('edit/<int:pk>/', PostEditView.as_view(), name='post_edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('subscribe_me1/', subscribe_me1, name='subscribe_me1'),
    path('subscribe_me2/', subscribe_me2, name='subscribe_me2'),
    path('subscribe_me3/', subscribe_me3, name='subscribe_me3'),
    path('subscribe_me4/', subscribe_me4, name='subscribe_me4'),
    path('accounts/', include('allauth.urls')),
]
