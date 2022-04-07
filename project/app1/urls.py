from django.urls import path, include
from .views import AddressesListView, Orders, PageView, PageView2

urlpatterns = [
    path('/', AddressesListView.as_view()),
    path('/create/', Orders.as_view()),
    path('/main/', PageView.as_view()),
    path('/information/', PageView2.as_view()),
]
