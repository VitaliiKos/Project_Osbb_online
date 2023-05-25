from django.urls import path

from .views import MeterCreateListReadingsView, MeterListCreateView, MeterRetrieveUpdateDestroyView

urlpatterns = [
    path('', MeterListCreateView.as_view(), name='meter_list_create'),
    path('/<int:pk>', MeterRetrieveUpdateDestroyView.as_view(), name='meter_delete_update'),

    path('/<int:pk>/readings', MeterCreateListReadingsView.as_view(), name='meter_readings_list_create')
]
