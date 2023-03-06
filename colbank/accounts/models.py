from django.db import models

# Create your models here.

class Account(models.Model):
    pass
class Customer(models.Model):
    pass

class Transfer(models.Model):
    pass

class Widthrawal(models.Model):
    pass

class Deposit(models.Model):
    account_id = model.models.ForeignKey("Account", verbose_name=_(""), on_delete=models.CASCADE)
    amount = model.models.DecimalField( max_digits=10, decimal_places=2)
    date_created = models.models.DateField( auto_now_add=True)
    
