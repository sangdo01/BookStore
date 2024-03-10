from django.db import models
from django.contrib.auth.models import User
from .profile import *


# class Author(models.Model):
#     name = models.CharField(max_length=250)
#     avatar = models.CharField(null=True, blank=True)
#     gender = models.CharField(null=True, blank=True)
    

# Nha cung cap
class Supplier(models.Model):
    name = models.CharField(max_length=250)


# Nha xuat ban
class Publisher(models.Model):
    name = models.CharField(max_length=250)
    logo = models.CharField(null=True, blank=True)
    status = models.BooleanField(default=True)


#Nhom danh muc san pham
class CategoryGroup(models.Model):
    name = models.CharField(max_length=250)


class Category(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(CategoryGroup, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=250)
    prices = models.DecimalField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    images = models.CharField(null=True, blank=True)
    # rating = models.DecimalField(max_length=20, null=True, blank=True)
    publication_year = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=250, null=True, blank=True)
    weight = models.DecimalField(null=True, blank=True)
    is_hot_selling = models.BooleanField(default=False, null=True, blank=True)
    # rating = models.ForeignKey(Rating, on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    publish_by = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    supply_by = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    created_at= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.BooleanField(default=True)


class Rating(models.Model):
    vote = models.IntegerField(default=0, null=True)
    comment = models.CharField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)





