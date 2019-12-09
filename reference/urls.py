from django.urls import path
from reference.views import *


urlpatterns = [
    path('all', ReferenceView.as_view(), name='all-references'),

    path('manufacturer/<int:pk>', ManufacturerDetail.as_view(), name='manufacturer-detail-view'),
    path('serie/<int:pk>', SerieDetail.as_view(), name='serie-detail-view'),

    path('manufacturer/', ManufacturerList.as_view(), name='manufacturer-list-view'),
    path('serie/', SerieList.as_view(), name='serie-list-view'),

    path('manufacturer-create/', ManufacturerCreate.as_view(), name='manufacturer-create-view'),
    path('serie-create/', SerieCreate.as_view(), name='serie-create-view'),

    path('manufacturer-update/<int:pk>', ManufacturerUpdate.as_view(), name='manufacturer-update-view'),
    path('serie-update/<int:pk>', SerieUpdate.as_view(), name='serie-update-view'),

    path('manufacturer-delete/<int:pk>', ManufacturerDelete.as_view(), name='manufacturer-delete-view'),
    path('serie-delete/<int:pk>', SerieDelete.as_view(), name='serie-delete-view'),
]
