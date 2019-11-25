from django.contrib import admin
from django.urls import path

from core.views import (
    prod_list,
    prod_detail,
)

app_name = 'core'

urlpatterns = [
    path('', prod_list, name='product_list'),
    path('<str:category_slug>/', prod_list, name='prod_list_by_category'),
    path('<int:id>/<str:slug>/', prod_detail, name='prod_detail')
    ]