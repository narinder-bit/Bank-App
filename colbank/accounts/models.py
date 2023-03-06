from django.db import models

# Create your models here.

class Account(models.Model):
    pass
class Customer(models.Model):
    pass

class Transfer(models.Model):
    pass
class Widthrawal(models.Model):

     account_id = models.ForeignKey('Account', on_delete=models.RESTRICT, null=True)
     amount = models.DecimalField(max_digits=8,decimal_places=2)
     date_created = models.DateField(auto_now_add=True)
     
class Deposit(models.Model):
    pass