from django.forms import ModelForm
from . models import Product, Client, Cart, Quantity

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'

class QuantityForm(ModelForm):
    class Meta:
        model = Quantity
        fields = '__all__'