from django.urls import path

from .views import MeterReadingsListCreateView, MeterReadingsRetrieveUpdateDestroyView

urlpatterns = [
    path('', MeterReadingsListCreateView.as_view(), name='meter_readings_list_create'),
    path('/<int:pk>', MeterReadingsRetrieveUpdateDestroyView.as_view(), name='meterReadings_delete_update'),
]
