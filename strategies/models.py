from django.db import models
from django.contrib.auth import get_user_model

from brokerage.models import Broker


class BasicOption(models.Model):
    ticker = models.CharField(max_length=5)
    open_date = models.DateTimeField()
    close_date = models.DateTimeField(null=True, blank=True)
    exp_date = models.DateTimeField()
    longshort = models.CharField(max_length=5, choices=(('long', 'Long'), ('short', 'Short')), default='long')
    callput = models.CharField(max_length=4, choices=(('call', 'Call'), ('put', 'Put')), default='call')
    strike = models.DecimalField(decimal_places=2, max_digits=10)
    premium = models.DecimalField(decimal_places=2, max_digits=10)
    count = models.PositiveSmallIntegerField()
    stock_price = models.DecimalField(decimal_places=2, max_digits=10)
    fees = models.DecimalField(decimal_places=2, max_digits=10)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=9, choices=(('closed', 'Closed'), ('open', 'Open'), ('exercised', 'Exercised')), default='open')
