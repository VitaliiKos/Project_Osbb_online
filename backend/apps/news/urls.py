from django.urls import path

from .views import (
    CommentDestroyView,
    CommentListCreateView,
    NewsCreateView,
    NewsDestroyView,
    NewsListView,
    NewsRetrieveView,
)

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('/create', NewsCreateView.as_view(), name='news_list_create'),
    path('/<int:pk>', NewsRetrieveView.as_view(), name='news_retrieve'),
    path('/<int:pk>/delete', NewsDestroyView.as_view(), name='news_destroy'),

    path('/<int:pk>/comments', CommentListCreateView.as_view(), name='news_list_create'),
    path('/comments/<int:pk>', CommentDestroyView.as_view(), name='news_comment_destroy'),


]
