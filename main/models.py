from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cartname = models.CharField(max_length=255)
    store_wheretobuy = models.CharField(max_length=255)
    date_for_notification = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cartname

class ListItem(models.Model):
    list_id = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, db_column='cart_id')

    def calculate_total(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.productname} - {self.quantity} {self.category}"  