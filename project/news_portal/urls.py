from django.urls import path
from .views import PostDetailView, PostsListView, PostsSearchListView, PostAddView, PostEditView, PostDeleteView


urlpatterns = [
    path('', PostsListView.as_view()),
    path('search/', PostsSearchListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('add/', PostAddView.as_view(), name='post_add'),
    path('edit/<int:pk>/', PostEditView.as_view(), name='post_edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete')
]
