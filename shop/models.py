from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    title = models.CharField(max_length=100)

class product(models.Model):
    title = models.CharField(max_length=100)
    contetnt = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits= 10)
    image = models.ImageField()
    quantity = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  #auto_now_add اتوماتیک ذخیره شده و قابل ویرایش نیست.
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    
    
class cart(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class order(models.Model):
    total_price = models.DecimalField(decimal_places=2, max_digits= 10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class order_products(models.Model):
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits= 10)
    # status = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    
class payment(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits= 10)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    error_code = models.CharField(max_length=200)
    
    
        