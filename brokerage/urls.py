from django.urls import path, include
from .views import *

app_name = 'broker'

urlpatterns = [
    path('manage/', manage, name='manage'),
    path('add/', BrokerCreateView.as_view(), name='add'),
    path('update/<int:pk>/', BrokerUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BrokerDeleteView.as_view(), name='delete'),
]
