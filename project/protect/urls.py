from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('accounts/profile/', IndexView.as_view()),
]
