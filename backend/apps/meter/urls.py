from django.urls import path

from .views import (
    MeterCreateListReadingsView,
    MeterListView,
    MeterPhotoCreateView,
    MeterPhotoDeleteView,
    MeterRetrieveUpdateDestroyView,
    MeterTypeCreateView,
    MeterTypeListView,
    MeterTypeRetrieveUpdateDestroyView,
    UserMeterCreateView,
)

urlpatterns = [
    path('', MeterListView.as_view(), name='meter_list'),
    path('/<int:pk>/create', UserMeterCreateView.as_view(), name='meter_list_create'),
    path('/<int:pk>', MeterRetrieveUpdateDestroyView.as_view(), name='meter_delete_update'),
    path('/<int:pk>/readings', MeterCreateListReadingsView.as_view(), name='meter_readings_list_create'),

    path('/type', MeterTypeListView.as_view(), name='meter_type_list'),
    path('/type/create', MeterTypeCreateView.as_view(), name='meter_type_create_list'),
    path('/type/<int:pk>', MeterTypeRetrieveUpdateDestroyView.as_view(), name='meter_type_update_destroy'),

    path('/<int:pk>/photo', MeterPhotoCreateView.as_view(), name='meter_add_photo'),
    path('/photo/<int:pk>', MeterPhotoDeleteView.as_view(), name='meterReading_photo_delete'),

]
