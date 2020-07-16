from django.contrib import admin

from .models import Product, Category, Order, Order_item, Coupon_Dis

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(Coupon_Dis)