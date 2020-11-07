from django.urls import path, include
from .views import *

app_name = 'strategies'

urlpatterns = [
    # path('manage/', manage, name='manage'),

    path('basic/add/', BasicOptionCreateView.as_view(), name='add_basic'),
    path('basic/update/<int:pk>/', BasicOptionUpdateView.as_view(), name='update_basic'),
    path('basic/delete/<int:pk>/', BasicOptionDeleteView.as_view(), name='delete_basic'),

    path('spread/add/', SpreadOptionCreateView.as_view(), name='add_spread'),
    path('spread/update/<int:pk>/', BasicOptionUpdateView.as_view(), name='update_spread'),
    path('spread/delete/<int:pk>/', SpreadOptionDeleteView.as_view(), name='delete_spread'),
]