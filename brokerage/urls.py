from django.urls import path, include
from .views import *

urlpatterns = [
    path('manage/', manage, name='broker_manage'),
    path('add/', BrokerCreateView.as_view(), name='broker_add'),
    path('update/<int:pk>/', BrokerUpdateView.as_view(), name='broker_update'),
    path('delete/<int:pk>/', BrokerDeleteView.as_view(), name='broker_delete'),
]
