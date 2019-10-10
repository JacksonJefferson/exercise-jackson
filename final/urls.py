from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.product_list),
    path('products/create', views.product_create),
    path('products/<int:id>/cart', views.cart_product),

]