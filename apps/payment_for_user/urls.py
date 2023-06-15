from django.urls import path

from .views import PaymentListCreateView

urlpatterns = [

    path('/<int:pk>', PaymentListCreateView.as_view(), name='payment_list_create'),
    # path('/create', NewsListCreateView.as_view(), name='news_list_create'),
    # path('/<int:pk>', NewsRetrieveView.as_view(), name='news_retrieve'),
    # path('/<int:pk>/delete', NewsDestroyView.as_view(), name='news_destroy'),
    #
    # path('/<int:pk>/comments', CommentListCreateView.as_view(), name='news_list_create'),

]
