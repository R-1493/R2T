from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    is_customer=models.BooleanField('is customer', default=False)# 'is customer' is try
    is_translator=models.BooleanField('is translator', default=False)# 'is customer' is try

class Translatorr(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,
    primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)   
    phoneNumber = models.CharField(max_length=17)
    First_Language = models.CharField(max_length=3)
    Second_Language = models.CharField(max_length=3)
    price = models.IntegerField(null=False, default=0)
    Certification = models.CharField(max_length=4)
    
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    First_Language = models.CharField(max_length=3)
    phoneNumber = models.CharField(max_length=17)

class Appointment(models.Model):
    customerName = models.CharField(max_length=50)
    translatorName = models.CharField(max_length=50)
    customerID = models.CharField(max_length=200)
    translatorID = models.CharField(max_length=200)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    
from datetime import datetime


class Room(models.Model):
    roomID = models.CharField(max_length=1000000)
    translator=models.CharField(max_length=50)
    customer=models.CharField(max_length=50)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    sender = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
   


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents
    date = models.DateTimeField(default=datetime.now , blank = True)

    def __str__(self):
        return self.name
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price/100)
