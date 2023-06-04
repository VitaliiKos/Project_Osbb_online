from django.urls import path

from .views import (
    FaultChangeStatusToActiveView,
    FaultChangeStatusToDoneView,
    FaultCommentListCreateView,
    FaultCommentUpdateDestroyView,
    FaultListCreateView,
    FaultRetrieveView,
)

urlpatterns = [
    path('', FaultListCreateView.as_view(), name='fault_list_create'),
    path('/<int:pk>/update', FaultRetrieveView.as_view(), name='fault_get_retrieve'),
    path('/<int:pk>/comments', FaultCommentListCreateView.as_view(), name='fault_comments_create_list'),
    path('/comments/<int:pk>', FaultCommentUpdateDestroyView.as_view(), name='fault_comments_update'),


    path('/<int:pk>/status_done', FaultChangeStatusToDoneView.as_view(), name='fault_partial_status_to_done'),
    path('/<int:pk>/status_active', FaultChangeStatusToActiveView.as_view(), name='fault_partial_status_to_active'),
]
