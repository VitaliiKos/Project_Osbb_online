from rest_framework.serializers import ModelSerializer, RelatedField

from core.dataclasses.meter_dataclass import Meter

from .models import MeterReadingsModel, MeterReadingsPhotoModel


class MeterRelatedFieldSerializer(RelatedField):

    def to_representation(self, value: Meter):
        return {'id': value.id, 'serial_number': value.serial_number, 'type': value.type}


class MeterReadingsPhotoSerializer(ModelSerializer):
    class Meta:
        model = MeterReadingsPhotoModel
        fields = ('id', 'photo',)

    def to_representation(self, instance):
        return instance.photo.url


class MeterReadingsSerializer(ModelSerializer):
    meter = MeterRelatedFieldSerializer(read_only=True)
    photos = MeterReadingsPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = MeterReadingsModel
        fields = ('id', 'reading', 'meter', 'photos', 'created_at', 'updated_at')
