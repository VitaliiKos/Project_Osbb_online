from django.urls import path

from .views import PollCreateListVoteView, PollCreateView, PollDestroyView, PollListView, PollRetrieveView

urlpatterns = [
    path('', PollListView.as_view(), name='poll_list'),
    path('/create', PollCreateView.as_view(), name='poll_list_create'),

    path('/<int:pk>', PollRetrieveView.as_view(), name='poll_retrieve'),
    path('/<int:pk>/delete', PollDestroyView.as_view(), name='poll_destroy'),
    path('/<int:pk>/vote', PollCreateListVoteView.as_view(), name='poll_cote_creat'),

]
