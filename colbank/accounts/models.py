from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    pass
class Customer(models.Model):
     # Fields
     user_name = models.CharField(max_length=20, help_text='Enter  username')
     user_email = models.CharField(max_length=20, help_text='Enter email address')
     user= models.ForeignKey(User, on_delete=models.CASCADE)
     

class Transfer(models.Model):
    pass

class Widthrawal(models.Model):
    pass

class Deposit(models.Model):
    pass