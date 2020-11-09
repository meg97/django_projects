from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def main_page(request):
	return HttpResponse("<h1> We have 4 links to show you some pages of our little project, lets try them! </h1> \
		<h2> <a href=/greeting>greeting</a> \
		<a href=/introduction>introduction</a> \
		<a href=/date>date</a> \
		<a href=/square>square</a> </h2>")

def greeting(request):
	return HttpResponse("<h1> Hallo, welcome to my second DJango project. I promise, that you won't \
		get bored here </h1> \
		<a href=http://127.0.0.1:8000>back</a>")

def introduction(request):
	return HttpResponse("<h1>This is a page for our lessons. You can find here today's Date if you want. Just \
		click on the 'date' button and you can see it</h1> \
		<a href=http://127.0.0.1:8000>back</a>")

def date(request):
	this_date = datetime.now()
	return HttpResponse(f"<h1>Today's Date is {this_date}</h1>\
		<a href=http://127.0.0.1:8000>back</a>")

def square(request):
	dict_1 = {}
	for i in range(1,16):
		dict_1[i] = i**2

	return HttpResponse(f'<h1>{dict_1}</h1>\
		<a href=http://127.0.0.1:8000>back</a>')