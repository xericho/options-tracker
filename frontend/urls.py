from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('get_option_data', get_option_data, name='get_option_data'),
]
