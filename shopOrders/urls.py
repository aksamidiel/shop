from django.urls import path
from .views import order_create

app_name = "shopOrders"

urlpatterns = [
    path('create/', order_create, name='order_create')
]
