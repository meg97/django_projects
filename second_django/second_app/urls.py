from django.urls import path
from .views import main_page, greeting, introduction, date, square


urlpatterns = [
	path('', main_page, name = "main_page"),
    path('greeting/', greeting, name = "greeting"),    
    path('introduction/', introduction, name = "introduction"),
    path('date/', date, name = "date"),
    path('square/', square, name = "square"),
]