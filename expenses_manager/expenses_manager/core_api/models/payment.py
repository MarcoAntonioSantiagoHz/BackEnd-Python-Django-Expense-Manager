
from django.db import models

from core_api.constants.category import CATEGORY_CHOICES
from core_api.models.expense import Expense


from .account import Account  # Account relationship
from core_api.constants.status import STATUS_CHOICES # constants
from django.db import models
from .account import Account
from .expense import Expense
from core_api.constants.status import STATUS_CHOICES
  
class Payment(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='payments')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(null=True, blank=True)
    method = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
