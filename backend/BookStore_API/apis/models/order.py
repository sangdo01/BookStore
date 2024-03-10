from django.db import models
from django.contrib.auth.models import User
from .profile import *
from .product import *
from BookStore_API.globals import *


class AddressStatus(models.Model):
    status = models.CharField(choices=ADDRESS_STATUS)


class Address(models.Model):
    street_number = models.CharField(null=True, blank=True)
    street_name = models.CharField(null=True, blank=True)
    city = models.CharField(null=True, blank=True)
    status_id = models.ForeignKey(AddressStatus, on_delete=models.SET_NULL, null=True, blank=True)
    custommer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Payment(models.Model):
    name = models.CharField(choices=PAYMENT_METHOD, null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    payment_amount = models.DecimalField(null=True, blank=True)
    status = models.CharField(choices=STATUS_PAYMENT, null=True, blank=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    # total_amount = models.DecimalField(null=True, blank=True)
    status_id = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True, blank=True)


class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_item_price = models.DecimalField(null=True, blank=True)
    order_item_quantity = models.IntegerField()



# class Cart(models.Model):
#     pass


# class Shipment(models.Model):
#     pass


class OrderStatus(models.Model):
    status_value = models.CharField(choices=STATUS_ORDER)


class OrderHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    status_id = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True, blank=True)
    date_date = models.DateTimeField(null=True, blank=True)









