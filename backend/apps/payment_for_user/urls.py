from django.urls import path

from .views import PaymentListCreateView, StandardPaymentListCreateView

urlpatterns = [

    path('/<int:pk>', PaymentListCreateView.as_view(), name='payment_list_create'),
    path('/standart_reciept', StandardPaymentListCreateView.as_view(), name='standard_payment_list_create'),
]
