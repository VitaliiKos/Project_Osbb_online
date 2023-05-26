from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from apps.meter.serialezers import MeterReadingsSerializer
from apps.readings.filters import MeterReadingFilter
from apps.readings.models import MeterReadingsModel, MeterReadingsPhotoModel
from apps.readings.serializer import MeterReadingsPhotoSerializer


class MeterReadingsListCreateView(ListAPIView):
    queryset = MeterReadingsModel.objects.all()
    serializer_class = MeterReadingsSerializer
    filterset_class = MeterReadingFilter


class MeterReadingsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = MeterReadingsModel.objects.all()
    serializer_class = MeterReadingsSerializer


class MeterReadingsAddPhotosView(GenericAPIView):
    queryset = MeterReadingsModel.objects.all()

    def post(self, *args, **kwargs):
        files = self.request.FILES
        meter_readings = self.get_object()
        for key in files:
            serializer = MeterReadingsPhotoSerializer(data={'photo': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(meter_readings=meter_readings)
        serializer = MeterReadingsSerializer(meter_readings)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MeterReadingsPhotoDeleteView(DestroyAPIView):
    queryset = MeterReadingsPhotoModel.objects.all()

    def perform_destroy(self, instance):
        instance.photo.delete()
        super().perform_destroy(instance)
