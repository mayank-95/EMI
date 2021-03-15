from django.db import models

# Create your models here.
from django.db import models


class Accounts(models.Model):
    name = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200)
    bank_account_number = models.CharField(max_length=15)


class Payments(models.Model):
    account = models.ForeignKey(Accounts,on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    transaction_date = models.DateTimeField('transaction date')
    accounting_period = models.DateField('accounting period')
