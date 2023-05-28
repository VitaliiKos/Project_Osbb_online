from rest_framework.serializers import ModelSerializer

from apps.readings.serializer import MeterReadingsSerializer

from .models import MeterModel


class MeterSerializer(ModelSerializer):
    readings = MeterReadingsSerializer(many=True, read_only=True)

    class Meta:
        model = MeterModel
        fields = ('id', 'serial_number', 'type', 'readings', 'user', 'created_at', 'updated_at')
