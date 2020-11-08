from django.urls import path
from .views import greeting, introduction, date, square


urlpatterns = [
    path('greeting/', greeting, name = "greeting"),    
    path('introduction/', introduction, name = "introduction"),
    path('date/', date, name = "date"),
    path('square/', square, name = "square"),
]