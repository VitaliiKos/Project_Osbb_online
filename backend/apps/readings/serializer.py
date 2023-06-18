from rest_framework.serializers import ModelSerializer

from .models import MeterReadingsModel


class MeterReadingsSerializer(ModelSerializer):
    class Meta:
        model = MeterReadingsModel
        fields = ('id', 'reading', 'meter', 'user', 'created_at', 'updated_at')
        read_only_fields = ('meter', 'user')
