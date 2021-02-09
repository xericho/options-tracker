from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

BROKERS = (
    ('TD', 'TD Ameritrade'),
    ('RH', 'Robinhood'),
)


class Broker(models.Model):
    name = models.CharField(max_length=50)
    broker = models.CharField(max_length=15, choices=BROKERS, default='RH')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    open_date = models.DateField(null=True, default=datetime.now)
    account_id = models.CharField(max_length=9, null=True)
    last_synced = models.DateField(null=True)

    def __str__(self):
        return self.name
