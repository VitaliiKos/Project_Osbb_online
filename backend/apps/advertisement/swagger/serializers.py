from apps.advertisement.serializers import AdvertisementSerializer


class SwaggerAdvertisementSerializer(AdvertisementSerializer):
    class Meta(AdvertisementSerializer.Meta):
        fields = ('id', 'title', 'body', 'phone', 'is_moderated', 'photos', 'created_at', 'user')
