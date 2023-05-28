from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from apps.advertisement.models import AdvertisementModel, AdvertisementPhotoModel
from apps.advertisement.serializers import AdvertisementPhotoSerializer, AdvertisementSerializer
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class AdvertisementListView(ListAPIView):
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (AllowAny,)


class AdvertisementCreateView(CreateAPIView):
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)


class AdvertisementRetrieveView(RetrieveAPIView):
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (AllowAny,)


class AdvertisementDestroyView(DestroyAPIView):
    queryset = AdvertisementModel.objects.all()
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        advertisement = self.get_object()
        if (advertisement.user != request.user) or advertisement.user['is_staff']:
            return Response(status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(advertisement)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdvertisementAddPhotosView(GenericAPIView):
    queryset = AdvertisementModel.objects.all()

    def post(self, *args, **kwargs):
        files = self.request.FILES
        advertisement = self.get_object()
        for key in files:
            serializer = AdvertisementPhotoSerializer(data={'photo': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(advertisement=advertisement)
        serializer = AdvertisementSerializer(advertisement)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdvertisementPhotoDeleteView(DestroyAPIView):
    queryset = AdvertisementPhotoModel.objects.all()

    def perform_destroy(self, instance):
        instance.photo.delete()
        super().perform_destroy(instance)


class ActivateAdvertisementView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    queryset = AdvertisementModel.objects.all()

    def patch(self, *args, **kwargs):
        advertisement = self.get_object()

        if advertisement.is_moderated:
            return Response('Error occurred while is_moderated==True.', status=status.HTTP_400_BAD_REQUEST)

        advertisement.is_moderated = True
        advertisement.save()
        serializer = AdvertisementSerializer(advertisement)
        return Response(serializer.data, status=status.HTTP_200_OK)
