from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.
class companys(models.Model):
    cmpnyid = models.AutoField(primary_key=True)
    cmpnyname = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    businessname =  models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobno = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    logo = models.ImageField(default = "default.png", upload_to="images")
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
