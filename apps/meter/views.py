from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.meter.models import MeterModel
from apps.readings.serializer import MeterReadingsSerializer

from .filters import MeterFilter
from .serialezers import MeterSerializer


class MeterListCreateView(ListCreateAPIView):
    queryset = MeterModel.objects.all()
    serializer_class = MeterSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = MeterFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MeterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = MeterModel.objects.all()
    serializer_class = MeterSerializer


class MeterCreateListReadingsView(CreateAPIView):
    queryset = MeterModel.objects.all()
    serializer_class = MeterReadingsSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        meter = self.get_object()
        serializer.save(meter=meter)

    def get(self, *args, **kwargs):
        meter = self.get_object()
        serializer = self.serializer_class(meter.readings, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
