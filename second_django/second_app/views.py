from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def greeting(request):
	return HttpResponse("Hallo, welcome to my second DJango project. I promise, that you won't \
		boring here")

def introduction(request):
	return HttpResponse("This is a page for our lessons. You can find here today's Date if you want. Just \
		write 'date' in url and you can see it")

def date(request):
	this_date = datetime.now()
	return HttpResponse(f"Today's Date is {this_date}")

def square(request):
	dict_1 = {}
	for i in range(1,16):
		dict_1[i] = i**2

	return HttpResponse(f'{dict_1}')