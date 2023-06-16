from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from apps.meter.models import MeterModel, MeterPhotoModel, MeterTypeModel
from apps.readings.serializer import MeterReadingsSerializer

from ..readings.models import MeterReadingsModel
from .filters import MeterFilter
from .serialezers import MeterPhotoSerializer, MeterSerializer, MeterTypeSerializer


class MeterListView(ListAPIView):
    serializer_class = MeterSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = MeterFilter

    def get_queryset(self):
        user_is_staff = self.request.user.is_staff
        if user_is_staff:
            return MeterModel.objects.all()
        return MeterModel.objects.filter(user_id=self.request.user.pk)


class UserMeterCreateView(CreateAPIView):
    serializer_class = MeterSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = MeterFilter

    def perform_create(self, serializer):
        user = self.request.user
        meter_specify_id = self.kwargs['pk']
        meter_specify = get_object_or_404(MeterTypeModel, id=meter_specify_id)
        meter = MeterModel.objects.filter(meter_specify_id=meter_specify_id, user_id=user.id)
        if meter:
            return Response('You have already meter', status.HTTP_403_FORBIDDEN)

        serializer.save(user=self.request.user, meter_specify=meter_specify)


class MeterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = MeterSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MeterModel.objects.filter(user_id=self.request.user.id)


class MeterCreateListReadingsView(CreateAPIView):
    queryset = MeterModel.objects.all()
    serializer_class = MeterReadingsSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        meter = get_object_or_404(MeterModel, id=self.kwargs['pk'], user_id=self.request.user.id)
        serializer.save(user=self.request.user, meter=meter)

    def get(self, *args, **kwargs):
        meter = self.get_object()
        serializer = self.serializer_class(meter.readings, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class MeterTypeListView(ListAPIView):
    queryset = MeterTypeModel.objects.all()
    serializer_class = MeterTypeSerializer
    permission_classes = (IsAuthenticated,)


class MeterTypeCreateView(CreateAPIView):
    serializer_class = MeterTypeSerializer
    permission_classes = (IsAdminUser,)


class MeterTypeRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = MeterTypeModel.objects.all()
    serializer_class = MeterTypeSerializer
    permission_classes = (IsAdminUser,)


class MeterPhotoCreateView(GenericAPIView):
    queryset = MeterPhotoModel.objects.all()

    def post(self, *args, **kwargs):
        files = self.request.FILES
        meter = get_object_or_404(MeterModel, id=self.kwargs['pk'])
        for key in files:
            serializer = MeterPhotoSerializer(data={'photo': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(meter=meter)
        serializer = MeterSerializer(meter)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MeterPhotoDeleteView(DestroyAPIView):
    queryset = MeterPhotoModel.objects.all()

    def perform_destroy(self, instance):
        instance.photo.delete()
        super().perform_destroy(instance)
