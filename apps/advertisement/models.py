from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.enums.regex_enum import RegEx
from core.services.upload_advertisement_service import upload_to

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class AdvertisementModel(models.Model):
    class Meta:
        db_table = 'advertisement'
        ordering = ('-created_at',)

    title = models.CharField(max_length=50, validators=[
        V.RegexValidator(RegEx.ADVERTISEMENT_TITLE.pattern, RegEx.ADVERTISEMENT_TITLE.msg)])
    body = models.TextField()
    phone = models.CharField(max_length=9, validators=[V.RegexValidator(RegEx.PHONE.pattern, RegEx.PHONE.msg)])
    is_moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')


class AdvertisementPhotoModel(models.Model):
    class Meta:
        db_table = 'advertisement_photo'
        ordering = ('id',)

    photo = models.ImageField(upload_to=upload_to, blank=True)
    advertisement = models.ForeignKey(AdvertisementModel, on_delete=models.CASCADE, related_name='photos')
