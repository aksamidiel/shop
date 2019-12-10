from django.urls import path
from userorder.views import *

urlpatterns = [
    path('userorder-create', OrderCheckOutView.as_view(), name='userorder-create'),
    path('userorder-success/<int:pk>', OrderSuccess.as_view(), name='userorder-success'),
    path('userorder-list', OrderList.as_view(), name='userorder-list'),
    path('userorder-update/<int:pk>', OrderUpdate.as_view(), name='userorder-update'),
    path('userorder-canceled/<int:pk>', OrderCanceled.as_view(), name='userorder-canceled'),
]