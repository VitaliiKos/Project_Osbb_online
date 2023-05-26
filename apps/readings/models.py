from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx
from core.services.upload_reading_service import upload_to

from apps.meter.models import MeterModel

from .managers import MeterReadingsManager


class MeterReadingsModel(models.Model):
    class Meta:
        db_table = 'readings'
        ordering = ('id',)

    reading = models.IntegerField(validators=[V.RegexValidator(RegEx.METER_READINGS.pattern, RegEx.METER_READINGS.msg)])
    meter = models.ForeignKey(MeterModel, on_delete=models.CASCADE, related_name='readings')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MeterReadingsManager.as_manager()


class MeterReadingsPhotoModel(models.Model):
    class Meta:
        db_table = 'meter_readings_photo'
        ordering = ('id',)

    photo = models.ImageField(upload_to=upload_to, blank=True)
    meter_readings = models.ForeignKey(MeterReadingsModel, on_delete=models.CASCADE, related_name='photos')
