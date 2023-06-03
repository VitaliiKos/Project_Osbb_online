from django.urls import path

from apps.poll.views import PollCreateListVoteView, PollCreateView, PollDestroyView, PollListView, PollRetrieveView

urlpatterns = [
    path('', PollListView.as_view(), name='poll_list'),
    path('/create', PollCreateView.as_view(), name='poll_list_create'),

    path('/<int:pk>', PollRetrieveView.as_view(), name='poll_retrieve'),
    path('/<int:pk>/delete', PollDestroyView.as_view(), name='poll_destroy'),
    path('/<int:pk>/vote', PollCreateListVoteView.as_view(), name='poll_cote_creat'),
    # path('/photo/<int:pk>', AdvertisementPhotoDeleteView.as_view(), name='poll_photo_delete'),
    # path('/<int:pk>/activate', ActivateAdvertisementView.as_view(), name='poll_activate'),

]
