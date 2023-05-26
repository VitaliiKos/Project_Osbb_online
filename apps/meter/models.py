from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class MeterModel(models.Model):
    class Meta:
        db_table = 'meter'
        ordering = ('id',)

    serial_number = models.CharField(max_length=20, unique=True, validators=[
        V.RegexValidator(RegEx.METER_SERIAL_NUMBER.pattern, RegEx.METER_SERIAL_NUMBER.msg)])
    type = models.CharField(max_length=20,
                            validators=[V.RegexValidator(RegEx.METER_TYPE.pattern, RegEx.METER_TYPE.msg)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='meter')
