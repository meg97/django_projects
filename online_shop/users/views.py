from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, ProfileUpdate
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os

# Create your views here.


def register(request):
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
            return redirect("main")
        else:
            messages.add_message(request, messages.WARNING, "User is not created successfully")

    return render(request, 'registration/user_register.html', {'form': form})

@login_required(login_url="login")
def user_profile(request):
    profile = Profile.objects.get(user_id = request.user.id)
    return render(request, "registration/user_profile.html", {"profile":profile})

@login_required(login_url="login")
def profile_update(request):
    profile = Profile.objects.get(user_id = request.user.id)
    form = ProfileUpdate(instance=profile)
    if request.method =="POST":
        form = ProfileUpdate(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            
                
            if request.FILES.get('user_image', None) != None:
                try:
                    os.remove(profile.user_image.url)
                except Exception as e:
                    print('Exception in removing old profile image: ', e)
                profile.user_image = request.FILES['user_image']
                profile.save()
            return redirect("user_profile")

        


    content = {'form':form}
    return render(request, "registration/user_profile_update.html", content)