from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [

    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user_profile/', user_views.user_profile, name='user_profile'),
    path('user_profile_update/', user_views.profile_update, name='profile_update'),

]