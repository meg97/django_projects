from django.db import models
from django.db.models import CharField, Model
from django.contrib.auth.models import User
from django_mysql.models import ListCharField
# from views import cart_view
# from django.shortcuts import render, redirect, get_object_or_404

STATUS_CHOICE = (
    (0, "Old"),
    (1, "New"),
)

class Category(models.Model):
	name = models.TextField()

	def __str__(self):
		return self.name
class Brand(models.Model):
	name = models.CharField(max_length = 60)
	def __str__(self):
		return self.name

class Item(models.Model):
	list_1 = ['product']
	name = models.CharField(max_length = 150)
	brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
	tags = models.TextField(blank = True)
	description = models.TextField(blank = True)
	item_image = models.ImageField(default="/media/no_image.jpg",  upload_to = 'media')
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	price = models.PositiveIntegerField(default=0)
	discount = models.PositiveIntegerField(default=0)
	color = models.CharField(max_length = 50, blank = True)
	status = models.IntegerField(choices=STATUS_CHOICE, default=1)
	ref_num = models.TextField(unique=True)
	def disc(self):
		answer = round(self.price*(1-self.discount/100), 2)
		return answer

	def __str__(self):
		return self.name

class OrderItem(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
	ordered = models.BooleanField(default = False)
	quantity = models.IntegerField(default = 1)
	order_item = models.ForeignKey(Item,  on_delete = models.CASCADE, blank = True, null = True)
	def __str__(self):
		return f"{self.order_item.name} quantity {self.quantity}"

	def get_item_total_price(self):
		if self.order_item.discount == 0:
			return self.quantity*self.order_item.price
		else:
			return self.quantity*self.order_item.disc()

class Order(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	items = models.ManyToManyField(OrderItem)
	ordered = models.BooleanField(default = False)
	def __str__(self):
		return str(self.user)

	def get_cart_total(self):
		total = 0
		
		for order_item in self.items.all():
			total += order_item.get_item_total_price()
		return total
