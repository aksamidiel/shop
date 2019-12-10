from django.urls import path
from escooters.views import *

urlpatterns = [
    path('all', EScooterList.as_view(), name='escooters-list-view'),
    path('escooters/<int:pk>', EScooterDetail.as_view(), name='escooters-detail-view'),
    path('escooters-create/', EScooterCreate.as_view(), name='escooters-create-view'),
    path('escooters-update/<int:pk>', EScooterUpdate.as_view(), name='escooters-update-view'),
    path('escooters-delete/<int:pk>', EScooterDelete.as_view(), name='escooters-delete-view'),
]