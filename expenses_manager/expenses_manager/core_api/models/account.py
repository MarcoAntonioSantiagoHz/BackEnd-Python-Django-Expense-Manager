from django.db import models

# created model for bd

class Account(models.Model): # we apply inheritance for models
    bank_name = models.CharField(max_length=100 )# short text with limit
    account_holder = models.CharField(max_length=100) # short text with limit
    current_balance = models.DecimalField(max_digits=15, decimal_places=2) #  Exact amount (DECIMAL(15,2) type), ideal for money
    account_number = models.CharField(max_length=50) # short text with limit
    is_active = models.BooleanField(default=True) # value boolean is real is not


