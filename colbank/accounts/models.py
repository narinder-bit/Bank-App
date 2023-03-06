from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# This model includes three fields: 'account_number', 'balance', and 'customer'.
# 'account_number' is a unique string that identifies the account
# 'balance' is a decimal number representing the account balance, and 'customer'
# is a foreign key relationship to the 'customer' model, indicating which customer owns the account.

class Account(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

    def __str__(self):
        return self.account_number

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