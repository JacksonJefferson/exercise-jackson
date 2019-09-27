from django.shortcuts import render, redirect
from . models import Product, Client, Cart, Quantity
from . forms import ProductForm, ClientForm, CartForm, QuantityForm


def home(request):
    return render (request, 'home.html')


def product_list(request):
    if (request.method == "POST"):
        search = request.POST.get('order')
        if (search == "name"):
            products = Product.objects.order_by('name')
            return render (request, 'product/list.html', {'products': products})
        elif (search == "smaller"):
            products = Product.objects.order_by('-value')
            return render (request, 'product/list.html', {'products': products})
        elif (search == "bigger"):
            products = Product.objects.order_by('value')
            return render (request, 'product/list.html', {'products': products})
        else:
            products = Product.objects.all()
            return render (request, 'product/list.html', {'products': products})
    else:
        products = Product.objects.all()
        return render (request, 'product/list.html', {'products': products})


