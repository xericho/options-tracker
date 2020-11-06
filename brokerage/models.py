from django.db import models
from django.contrib.auth import get_user_model


class Broker(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
