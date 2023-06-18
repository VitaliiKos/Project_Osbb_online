from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.meter.serialezers import MeterReadingsSerializer
from apps.readings.filters import MeterReadingFilter
from apps.readings.models import MeterReadingsModel


class MeterReadingsListCreateView(ListAPIView):
    """
        Get authorization user's list of meter_readings
        or
        get all list of meter_readings if user.is_staff == True
    """
    serializer_class = MeterReadingsSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = MeterReadingFilter

    def get_queryset(self):
        if self.request.user.is_staff:
            return MeterReadingsModel.objects.all()
        return MeterReadingsModel.objects.filter(user_id=self.request.user.pk)


class MeterReadingsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
        get:
            Get meter_readings by id
        put:
            Full Update meter_readings by id
        patch:
            Partial update meter_readings by id
        delete:
            Destroy meter_readings by id
    """
    queryset = MeterReadingsModel.objects.all()
    serializer_class = MeterReadingsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return MeterReadingsModel.objects.all()
        return MeterReadingsModel.objects.filter(user_id=self.request.user.pk)
