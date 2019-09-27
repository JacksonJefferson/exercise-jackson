from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.name

class Cart(models.Model):
    date = models.CharField(max_length=20)  
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Quantity(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    