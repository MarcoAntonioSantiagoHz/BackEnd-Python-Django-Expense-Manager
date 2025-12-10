# created model for bd

from django.db import models

from core_api.constants.category import CATEGORY_CHOICES

# core_api/models/expense.py
from django.db import models
from .account import Account
from core_api.constants.category import CATEGORY_CHOICES
from core_api.constants.status import STATUS_CHOICES

class Expense(models.Model):
  
    # Campos del modelo
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # name expense text limit 50
    description = models.CharField(max_length=100)  # description expense text limit 100
    date = models.DateTimeField()  # date expense/payment
    amount = models.DecimalField(max_digits=15, decimal_places=2)  # amount exactly
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES) # CATEGORIES: pending/approved/canceled
    status = models.CharField(max_length=20, choices=STATUS_CHOICES) # Status: pending/approved/canceled
    # type = models.CharField(max_length=50, choices=TYPE_CHOICES) # Type: expense or payment

