from django.utils.decorators import method_decorator

from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.advertisement.swagger.serializers import SwaggerAdvertisementSerializer


def advertisement_list_swagger():
    return method_decorator(swagger_auto_schema(responses={
        status.HTTP_200_OK: SwaggerAdvertisementSerializer()
    }, security=[]),
        'get'
    )


def activate_advertisement_swagger():
    return method_decorator(swagger_auto_schema(responses={
        status.HTTP_200_OK: SwaggerAdvertisementSerializer()
    }),
        'patch'
    )


def advertisement_add_photo_swagger():
    return method_decorator(swagger_auto_schema(responses={
        status.HTTP_201_CREATED: SwaggerAdvertisementSerializer()
    }),
        'post'
    )
