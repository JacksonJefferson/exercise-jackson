from django.shortcuts import render, redirect
from . models import Product, Client, Cart, Quantity
from . forms import ProductForm, ClientForm, CartForm, QuantityForm
import json



def home(request):
    visitor = request.session.get('visitor', 1001)
    request.session['visitor'] = visitor + 1
    return render (request, 'home.html')


def product_list(request):
    if (request.method == "POST"):
        search = request.POST.get('order')
        if (search == "name"):
            products = Product.objects.order_by('name')
            return render (request, 'product/list.html', {'products': products})
        elif (search == "smaller"):
            products = Product.objects.order_by('value')
            return render (request, 'product/list.html', {'products': products})
        elif (search == "bigger"):
            products = Product.objects.order_by('-value')
            return render (request, 'product/list.html', {'products': products})
        else:
            products = Product.objects.all()
            return render (request, 'product/list.html', {'products': products})
    else:
        products = Product.objects.all()
        return render (request, 'product/list.html', {'products': products})


def product_create(request):
    if (request.method == "POST"):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/final/products/')
        else:
            return render (request, 'product/create.html', {'form': form})
    else:
        form = ProductForm()
        return render (request, 'product/create.html', {'form': form})

def cart_product(request, id):
    product = Product.objects.get(pk=id)
    search ={
        'id':product.id,
        'name':product.name,
    }
    list_product = request.session.get('ss',[])
    list_product.append(search)
    request.session['ss']=list_product
    return redirect ('/final/products/')


