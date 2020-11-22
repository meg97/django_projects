from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.


def user_register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)

            if not user is None:
                login(request, user)
            messages.add_message(request, messages.SUCCESS, "User is created successfully")
            messages.add_message(request, messages.SUCCESS, "User is logged in")
            return redirect("home")
        else:
            messages.add_message(request, messages.WARNING, "User is not created successfully")

    return render(request, 'registration/user_register.html', {'form': form})
