from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=250)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    images = models.CharField(max_length=550, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=250, blank=True, null=True)
    role = models.ManyToManyField(Role, on_delete=models.CASCADE, blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    images = models.CharField(max_length=550, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=250, blank=True, null=True)
    # role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

