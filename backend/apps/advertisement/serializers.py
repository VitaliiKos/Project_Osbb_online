from rest_framework.serializers import ModelSerializer

from apps.advertisement.models import AdvertisementModel, AdvertisementPhotoModel


class AdvertisementPhotoSerializer(ModelSerializer):
    class Meta:
        model = AdvertisementPhotoModel
        fields = ('id', 'photo',)

    def to_representation(self, instance):
        return instance.photo.url


class AdvertisementSerializer(ModelSerializer):
    photos = AdvertisementPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = AdvertisementModel
        fields = ('id', 'title', 'body', 'phone', 'is_moderated', 'photos', 'created_at', 'user')
        read_only_fields = ('user',)
