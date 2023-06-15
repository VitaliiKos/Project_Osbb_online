from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx
from core.services.upload_reading_service import upload_to

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class MeterTypeModel(models.Model):
    class Meta:
        db_table = 'meter_type'
        ordering = ('id',)

    specify = models.CharField(max_length=150, unique=True)
    price = models.FloatField()

    # def __str__(self):
    #     return self.__dict__


class MeterModel(models.Model):
    class Meta:
        db_table = 'meter'
        ordering = ('id',)

    serial_number = models.CharField(max_length=20, unique=True, validators=[
        V.RegexValidator(RegEx.METER_SERIAL_NUMBER.pattern, RegEx.METER_SERIAL_NUMBER.msg)])
    meter_specify = models.ForeignKey(MeterTypeModel, on_delete=models.CASCADE, related_name='meter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='meter')


class MeterPhotoModel(models.Model):
    class Meta:
        db_table = 'meter_readings_photo'
        ordering = ('-created_at',)

    photo = models.ImageField(upload_to=upload_to, blank=True)
    meter = models.ForeignKey(MeterModel, on_delete=models.CASCADE, related_name='photos')
    created_at = models.DateTimeField(auto_now_add=True)
