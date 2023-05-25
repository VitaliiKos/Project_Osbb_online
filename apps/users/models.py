from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx
from core.services.upload_avatar_service import upload_to

from apps.users.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128,
                                validators=[V.RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.msg)])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20, validators=[V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    surname = models.CharField(max_length=20, validators=[V.RegexValidator(RegEx.SURNAME.pattern, RegEx.SURNAME.msg)])
    phone = models.CharField(max_length=9, validators=[V.RegexValidator(RegEx.PHONE.pattern, RegEx.PHONE.msg)])
    age = models.IntegerField(validators=[V.MinValueValidator(18), V.MaxValueValidator(150)])
    apartment_number = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(400)])
    avatar = models.ImageField(upload_to=upload_to, blank=True)
    # electricity_meter = models.ForeignKey(MeterModel, on_delete=models.CASCADE, related_name='electricity_meter',
    #                                       blank=True, default='sr0000')
    # gas_meter = models.ForeignKey(MeterModel, on_delete=models.CASCADE, related_name='gas_meter', blank=True,
    #                               default='sr0000')
    # water_meter = models.ForeignKey(MeterModel, on_delete=models.CASCADE, related_name='water_meter', blank=True,
    #                                 default='sr0000')
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
