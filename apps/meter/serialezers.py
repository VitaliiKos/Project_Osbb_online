from rest_framework.serializers import ModelSerializer

from apps.readings.serializer import MeterReadingsSerializer

from .models import MeterModel, MeterPhotoModel, MeterTypeModel


class StandardMeterTypeSerializer(ModelSerializer):
    class Meta:
        model = MeterTypeModel
        fields = ('id', 'specify', 'price')


class MeterTypeSerializer(ModelSerializer):
    class Meta:
        model = MeterTypeModel
        fields = ('id', 'specify', 'price')


class MeterPhotoSerializer(ModelSerializer):
    class Meta:
        model = MeterPhotoModel
        fields = ('id', 'photo',)

    def to_representation(self, instance):
        return instance.photo.url


class MeterSerializer(ModelSerializer):
    readings = MeterReadingsSerializer(many=True, read_only=True)
    photos = MeterPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = MeterModel
        fields = ('id', 'serial_number', 'meter_specify', 'photos', 'readings', 'user', 'created_at', 'updated_at')
        read_only_fields = ('user', 'meter_specify')
