from rest_framework.serializers import ModelSerializer

from .models import MeterReadingsModel

# from core.dataclasses.meter_dataclass import Meter


# class MeterRelatedFieldSerializer(RelatedField):
#
#     def to_representation(self, value: Meter):
#         return {'id': value.id, 'serial_number': value.serial_number}
#


class MeterReadingsSerializer(ModelSerializer):
    class Meta:
        model = MeterReadingsModel
        fields = ('id', 'reading', 'meter', 'user', 'created_at', 'updated_at')
        read_only_fields = ('meter', 'user')
