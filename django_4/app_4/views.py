from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import NewTask
from .forms import TaskForm
from django.contrib import messages

# Create your views here.

def main_page(self):
	return HttpResponse("<h1> Hello!!!! It's a new site, where you \
	 can register and write something you want to do</h1> \
     <h2> Here you can login to your existed page</h2>\
     <a href=/user/login>login</a> \
     <h2> And here you can register as a new user</h2> \
     <a href=/user/register>register</a>")

@login_required(login_url="login")
def home(request):
    tasks = NewTask.objects.all().filter(user=request.user)

    content = {'tasks': tasks}
    return render(request, "app_4/home.html", content)

@login_required(login_url="login")
def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = User.objects.get(id=request.user.id)
            task.save()
        messages.add_message(request, messages.SUCCESS, "Congratulations!!! You have a new task")

        return redirect('home')

    form = TaskForm()
    content = {'form': form}

    return render(request, "app_4/new_task.html", content)

def task_view(request,pk):
    task = NewTask.objects.get(id=pk)
    content = {'task': task}
    return render(request, "app_4/task_view.html", content)

def task_update(request,pk):
    task = NewTask.objects.get(id=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        messages.add_message(request, messages.SUCCESS, "Your task is updated")

        return redirect('home')

    form = TaskForm(instance=task)
    content = {'form': form}
    return render(request, "app_4/task_update.html", content)

def task_delete(request,pk):
    task = NewTask.objects.get(id=pk)
    task.delete()
    messages.add_message(request, messages.SUCCESS, "Ohh! You deleted your task!")
    return redirect("home")
