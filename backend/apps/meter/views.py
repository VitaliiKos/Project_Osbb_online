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

from .filters import MeterFilter
from .serialezers import MeterPhotoSerializer, MeterSerializer, MeterTypeSerializer


class MeterListView(ListAPIView):
    """
        Get user's meters or get all meters if user.is_staff==True
    """
    serializer_class = MeterSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = MeterFilter

    def get_queryset(self):
        user_is_staff = self.request.user.is_staff
        if user_is_staff:
            return MeterModel.objects.all()
        return MeterModel.objects.filter(user_id=self.request.user.pk)


class UserMeterCreateView(CreateAPIView):
    """
        Create user's meter by type of meter
    """
    serializer_class = MeterSerializer
    queryset = MeterModel.objects.all()
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
    """
       get:
           Get meter by id
       patch:
           Partial update meter by id
       put:
           Full update meter by id
       delete:
           Delete meter by id
       """
    serializer_class = MeterSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MeterModel.objects.filter(user_id=self.request.user.id)


class MeterCreateListReadingsView(CreateAPIView):
    """
        get:
            Get meter by id
        post:
            Create meter's reading
    """
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
    """
        Get meter's type list
    """
    queryset = MeterTypeModel.objects.all()
    serializer_class = MeterTypeSerializer
    permission_classes = (IsAuthenticated,)


class MeterTypeCreateView(CreateAPIView):
    """
        Create meter's type
    """
    serializer_class = MeterTypeSerializer
    permission_classes = (IsAdminUser,)


class MeterTypeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
        get:
            Get meter's type by id
        patch:
            Partial update meter's type by id
        put:
            Full update meter's type by id
        delete:
            Delete meter's type by id
    """
    queryset = MeterTypeModel.objects.all()
    serializer_class = MeterTypeSerializer
    permission_classes = (IsAdminUser,)


class MeterPhotoCreateView(GenericAPIView):
    """
        Add photo for meter
    """
    queryset = MeterPhotoModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        pass

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
    """
        Delete meter's photo
    """
    queryset = MeterPhotoModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_destroy(self, instance):
        instance.photo.delete()
        super().perform_destroy(instance)
