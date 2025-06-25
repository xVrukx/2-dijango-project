from django.db import models

# Create your models here.

class Contactus(models.Model):
    first_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    last_emailId = models.EmailField(max_length=20,blank=True,unique=True)
    mobile_no = models.IntegerField(max_length=10)
    address = models.TextField()


    
class store_name(models.Model):
 storename = models.CharField(max_length=20,blank=True)
 contact = models.BigIntegerField(max_length=10,blank=True)
 stars = models.CharField(max_length=5,blank=True
                          )
