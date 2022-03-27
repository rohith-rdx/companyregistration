from tkinter import CASCADE
from django.db import models
from app.models import *
from .models import *
# Create your models here.

# Create your models here.
class branchregister(models.Model):
    branchid = models.AutoField(primary_key=True)
    branchname = models.CharField(max_length=255)
    businessname =  models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobno = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    logo = models.ImageField(default = "default.png", upload_to="images")
    cmpnyid = models.ForeignKey(companys,on_delete=models.CASCADE)
    
class employee(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    branchname=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    pin=models.CharField(max_length=255)
    image=models.ImageField(default='default.png',upload_to="images")
    branchid=models.ForeignKey(branchregister, on_delete=models.CASCADE)
    