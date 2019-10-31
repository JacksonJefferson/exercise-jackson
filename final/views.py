from django.shortcuts import render, redirect
from . models import Product, Client, Cart, Quantity
from . forms import ProductForm, ClientForm, CartForm, QuantityForm
import json
from datetime import date



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
    list_product = request.session.get('ss',[])
    flag = False

    for s in list_product:
        if product.id == int(s['id']):
            p = {
                'id':product.id,
                'quantity':s['quantity']+1
            }
            flag = True
            list_product.remove(s)
            list_product.append(p)
    if flag == False:
        p = {
                'id':product.id,
                'quantity':1
            }
        list_product.append(p)
    
    request.session['ss']=list_product
    return redirect ('/final/products/')

def cart(request):
    car = request.session['ss']
    n = []
    soma = 0
    for i in car:
        product = Product.objects.get(pk=int(i['id']))
        val = product.value * int(i['quantity'])
        soma = soma + val
        p = {
                'id':product.id,
                'quantity':i['quantity'],
                'value':product.value,
                'value_total':val
            }
        n.append(p)
    return render (request, 'product/cart.html', {'n':n, 'soma':soma})

def check_out(request):
    s = request.session['ss']
    client = Client.objects.get(pk=1)
    date_actual = date.today()
    cart = Cart.objects.create(client=client,date=date_actual)
    Cart.save(cart)
    for i in s:
        product = Product.objects.get(pk=int(i['id']))
        quant = Quantity.objects.create(quantity=int(i['quantity']), product=product, cart=cart)
        Quantity.save(quant)
    del request.session['ss']
    return redirect('/final/products/')