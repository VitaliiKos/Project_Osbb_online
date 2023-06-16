from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx

from apps.meter.models import MeterModel
from apps.users.models import UserModel as User

from .managers import MeterReadingsManager

UserModel: User = get_user_model()


class MeterReadingsModel(models.Model):
    class Meta:
        db_table = 'readings'
        ordering = ('-created_at',)

    reading = models.IntegerField(validators=[V.RegexValidator(RegEx.METER_READINGS.pattern, RegEx.METER_READINGS.msg)])
    meter = models.ForeignKey(MeterModel, on_delete=models.CASCADE, related_name='reading')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MeterReadingsManager.as_manager()
