from django.urls import path

from .views import (
    MeterReadingsAddPhotosView,
    MeterReadingsListCreateView,
    MeterReadingsPhotoDeleteView,
    MeterReadingsRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', MeterReadingsListCreateView.as_view(), name='meterReadings_list_create'),
    path('/<int:pk>', MeterReadingsRetrieveUpdateDestroyView.as_view(), name='meterReadings_delete_update'),
    path('/<int:pk>/photo', MeterReadingsAddPhotosView.as_view(), name='meterReading_add_photo'),
    path('/photo/<int:pk>', MeterReadingsPhotoDeleteView.as_view(), name='meterReading_photo_delete'),
]
