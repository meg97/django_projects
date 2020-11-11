from django.urls import path
from .views import home, dict1

urlpatterns = [
    path('', home, name = "home"),
    path('/dict1', dict1, name = "dict1"),
]