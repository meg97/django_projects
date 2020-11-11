from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
	with open("template_app/django_json.json","r") as file_1:
		file = json.load(file_1)
		return httpResponse(f"file")

def dict1(request):
	d1 = {"a":100, "b":200,"c":300}
	d2 = {"a":300, "b":200,"d":400}
	d3 = {}
	for i,j in d1.items():
		pass
	for m,n in d2.items():
		if i == m:
			d3[i] = n+j
		elif i != m:
			d3[i] = j 
			
		return HttpResponse(f"d3")
