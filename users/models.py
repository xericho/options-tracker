from django.contrib.auth.models import AbstractUser
from django.db import models

EXP_LEVELS = (
    (1, 'Noob'),
    (2, 'Proficient'),
    (3, 'Experienced'),
)
class User(AbstractUser):
    trading_exp = models.PositiveSmallIntegerField(choices=EXP_LEVELS, default=1)
    date_joined = models.DateTimeField(auto_now_add=True)
