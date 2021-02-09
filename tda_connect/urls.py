from django.urls import path, include
from .views import *

app_name = 'tda'

urlpatterns = [
    path('sync/', SyncBroker.as_view(), name='sync'),
]
