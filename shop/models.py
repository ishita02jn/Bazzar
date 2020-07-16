from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    prod_id = models.AutoField
    prod_name = models.CharField(max_length = 50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) 
    subcategory = models.CharField(max_length = 50, default = "") 
    description = models.CharField(max_length = 300)
    price = models.IntegerField()  
    pub_date = models.DateField()
    image = models.ImageField(upload_to='prod-image/', default = "")

    def __str__(self): 
        return self.prod_name

class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self): 
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    shipping =  models.ForeignKey('Shipping_Address', on_delete=models.SET_NULL, null = True)
    transaction_id = models.CharField(null = True, max_length = 50)
    totalamt = models.IntegerField(default=None, null=True)
    trans_mode = models.CharField(max_length=30, default=None, null=True)
    coupon = models.ForeignKey('Coupon_Dis', on_delete=models.PROTECT, default=None, null=True)
    
    # def __str__(self): 
    #     return self.order_id

class Coupon_Dis(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    coupon_code = models.CharField(max_length=50)
    discount_percent = models.PositiveIntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(100)])
    
class Order_item(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)

    # def __str__(self): 
    #     return self.prod_id

class Shipping_Address(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length = 50)
    mobile = models.CharField(max_length=12) 
    pincode = models.CharField(max_length = 6) 
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 100) 
    state = models.CharField(max_length = 100)
    date_added = models.DateTimeField(auto_now_add = True)
