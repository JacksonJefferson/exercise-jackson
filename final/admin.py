from django.contrib import admin

from . models import Product, Client, Cart, Quantity

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Cart)
admin.site.register(Quantity)