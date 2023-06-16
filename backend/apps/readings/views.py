from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.meter.serialezers import MeterReadingsSerializer
from apps.readings.filters import MeterReadingFilter
from apps.readings.models import MeterReadingsModel


class MeterReadingsListCreateView(ListAPIView):
    serializer_class = MeterReadingsSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = MeterReadingFilter

    def get_queryset(self):
        if self.request.user.is_staff:
            return MeterReadingsModel.objects.all()
        return MeterReadingsModel.objects.filter(user_id=self.request.user.pk)


class MeterReadingsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = MeterReadingsModel.objects.all()
    serializer_class = MeterReadingsSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return MeterReadingsModel.objects.all()
        return MeterReadingsModel.objects.filter(user_id=self.request.user.pk)
