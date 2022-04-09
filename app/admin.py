from django.contrib import admin
from .models import *
from  django.contrib.auth.models  import  Group 
admin.site.unregister(Group) 

admin.site.site_header = 'Shopmandu'
# Register your models here.



admin.site.register(
    [Admin,Customer, Category, Product, Cart, CartProduct, Order, ProductImage, Wishlist])
