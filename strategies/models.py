from django.db import models
from django.contrib.auth import get_user_model

from brokerage.models import Broker


class BasicOption(models.Model):
    ticker = models.CharField(max_length=5)
    open_date = models.DateField()
    close_date = models.DateField(null=True, blank=True)
    exp_date = models.DateField()
    longshort = models.CharField(max_length=5, choices=(('long', 'Long'), ('short', 'Short')), default='long')
    callput = models.CharField(max_length=4, choices=(('call', 'Call'), ('put', 'Put')), default='call')
    strike = models.DecimalField(decimal_places=2, max_digits=10)
    premium = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveSmallIntegerField()
    stock_price = models.DecimalField(decimal_places=2, max_digits=10)
    fees = models.DecimalField(decimal_places=2, max_digits=10)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=9, choices=(('expired', 'Expired'), ('closed', 'Closed'), ('open', 'Open'), ('exercised', 'Exercised')), default='open')
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)


class SpreadOption(models.Model):
    ticker = models.CharField(max_length=5)
    open_date = models.DateField()
    close_date = models.DateField(null=True, blank=True)
    exp_date = models.DateField()
    creditdebit = models.CharField(max_length=6, choices=(('debit', 'Debit'), ('credit', 'Credit')), default='debit')
    callput = models.CharField(max_length=4, choices=(('call', 'Call'), ('put', 'Put')), default='call')
    strike1 = models.DecimalField(decimal_places=2, max_digits=10)
    strike2 = models.DecimalField(decimal_places=2, max_digits=10)
    premium = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveSmallIntegerField()
    stock_price = models.DecimalField(decimal_places=2, max_digits=10)
    fees = models.DecimalField(decimal_places=2, max_digits=10)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=9, choices=(('expired', 'Expired'), ('closed', 'Closed'), ('open', 'Open'), ('exercised', 'Exercised')), default='open')
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
