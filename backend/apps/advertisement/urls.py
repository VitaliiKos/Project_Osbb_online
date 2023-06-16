from django.urls import path

from .views import (
    ActivateAdvertisementView,
    AdvertisementAddPhotosView,
    AdvertisementCreateView,
    AdvertisementDestroyView,
    AdvertisementListView,
    AdvertisementPhotoDeleteView,
    AdvertisementRetrieveView,
)

urlpatterns = [
    path('', AdvertisementListView.as_view(), name='advertisement_list'),
    path('/<int:pk>', AdvertisementRetrieveView.as_view(), name='advertisement_retrieve'),
    path('/create', AdvertisementCreateView.as_view(), name='advertisement_list_create'),
    path('/<int:pk>/delete', AdvertisementDestroyView.as_view(), name='advertisement_destroy'),
    path('/<int:pk>/photo', AdvertisementAddPhotosView.as_view(), name='advertisement_add_photo'),
    path('/photo/<int:pk>', AdvertisementPhotoDeleteView.as_view(), name='advertisement_photo_delete'),
    path('/<int:pk>/activate', ActivateAdvertisementView.as_view(), name='advertisement_activate'),
]
