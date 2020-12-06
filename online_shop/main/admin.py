from django.contrib import admin
from .models import Category, Brand, Item, OrderItem, Order

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Brand)
admin.site.register(OrderItem)
admin.site.register(Order)
