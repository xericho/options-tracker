from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

from brokerage.models import Broker

STATUS = {
    'CLOSING': 'close',
    'OPENING': 'open',
}

# class BasicOption(models.Model):
#     ticker = models.CharField(max_length=5)
#     open_date = models.DateField(default=datetime.now)
#     close_date = models.DateField(null=True, blank=True)
#     exp_date = models.DateField(default=datetime.now)
#     longshort = models.CharField(max_length=5, choices=(('long', 'Long'), ('short', 'Short')), default='long')
#     callput = models.CharField(max_length=4, choices=(('call', 'Call'), ('put', 'Put')), default='call')
#     strike = models.DecimalField(decimal_places=2, max_digits=10)
#     premium = models.DecimalField(decimal_places=2, max_digits=10)
#     quantity = models.PositiveSmallIntegerField()
#     stock_price = models.DecimalField(decimal_places=2, max_digits=10)
#     close_price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
#     profitloss = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
#     fees = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
#     broker = models.ForeignKey(Broker, on_delete=models.CASCADE, null=True)
#     status = models.CharField(max_length=9, choices=(('expired', 'Expired'), ('closed', 'Closed'), ('open', 'Open'), ('exercised', 'Exercised')), default='open')
#     user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
#     order_id = models.CharField(max_length=15, null=True)
#

# class SpreadOption(models.Model):
#     ticker = models.CharField(max_length=5)
#     open_date = models.DateField(default=datetime.now)
#     close_date = models.DateField(null=True, blank=True)
#     exp_date = models.DateField(default=datetime.now)
#     creditdebit = models.CharField(max_length=6, choices=(('debit', 'Debit'), ('credit', 'Credit')), default='debit')
#     callput = models.CharField(max_length=4, choices=(('call', 'Call'), ('put', 'Put')), default='call')
#     strike1 = models.DecimalField(decimal_places=2, max_digits=10)
#     strike2 = models.DecimalField(decimal_places=2, max_digits=10)
#     premium = models.DecimalField(decimal_places=2, max_digits=10)
#     quantity = models.PositiveSmallIntegerField()
#     stock_price = models.DecimalField(decimal_places=2, max_digits=10)
#     close_price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
#     profitloss = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
#     fees = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
#     broker = models.ForeignKey(Broker, on_delete=models.CASCADE, null=True)
#     status = models.CharField(max_length=9, choices=(('expired', 'Expired'), ('closed', 'Closed'), ('open', 'Open'), ('exercised', 'Exercised')), default='open')
#     user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
#     order_id = models.CharField(max_length=15, null=True)



class Order(models.Model):
    cusip = models.CharField(max_length=15, null=True)
    ticker = models.CharField(max_length=5)
    transaction_date = models.DateField(null=True, blank=True)
    exp_date = models.DateField(default=datetime.now)
    longshort = models.CharField(null=True, max_length=5, choices=(('long', 'Long'), ('short', 'Short')), default=None)
    callput = models.CharField(null=True, max_length=4, choices=(('call', 'Call'), ('put', 'Put')), default=None)
    status = models.CharField(max_length=7, choices=(('open', 'Open'), ('close', 'Close'), ('expired', 'Expired')), default='open')
    quantity = models.PositiveSmallIntegerField()
    net_amount = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    total_fees = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

