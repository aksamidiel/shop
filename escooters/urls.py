from django.urls import path
from .views import *

urlpatterns = [
    path('all', EScooterList.as_view(), name='escooter-list-view'),
    path('escooter/<int:pk>', EScooterDetail.as_view(), name='escooter-detail-view'),
    path('escooter-create/', EScooterCreate.as_view(), name='escooter-create-view'),
    path('escooter-update/<int:pk>', EScooterUpdate.as_view(), name='escooter-update-view'),
    path('escooter-delete/<int:pk>', EScooterDelete.as_view(), name='escooter-delete-view'),
]