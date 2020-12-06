rom django import forms
from django.forms import ModelForm
from .models import NewItem

class ItemForm(ModelForm):
	class Meta:
		model = NewItem
		fields = '__all__'
