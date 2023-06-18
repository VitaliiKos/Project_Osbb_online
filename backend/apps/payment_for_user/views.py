from datetime import datetime

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.meter.models import MeterModel, MeterTypeModel, StandardMeterTypeModel
from apps.readings.models import MeterReadingsModel

from .models import PaymentModel, StandardPaymentModel
from .serializers import PaymentSerializer, StandardPaymentSerializer


class PaymentListCreateView(ListCreateAPIView):
    """
        get:
            Get authorization user's list of payment
            or
            get all list of payments if user.is_staff == True
        post:
            Create new payment
    """
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return PaymentModel.objects.all()
        return PaymentModel.objects.filter(user_id=self.request.user.id)

    def post(self, request, *args, **kwargs):
        current_date = datetime.now()
        meter = MeterModel.objects.get(id=self.kwargs['pk'], user_id=self.request.user.id)
        meter_type = get_object_or_404(MeterTypeModel, id=meter.meter_specify_id)
        readings = MeterReadingsModel.objects.get_readings_by_meter_id(meter.id)[:2]

        previous_reading = readings[1]
        current_reading = readings[0]

        current_reading_month = current_reading.created_at.month

        if current_date.month != current_reading_month:
            raise ValidationError('You have not provided a current score')

        payment = PaymentModel.objects.filter(user_id=self.request.user.id).first()
        if payment and current_date.month == payment.created_at.month and current_date.year == payment.created_at.year:
            serializer = self.get_serializer(payment)
            return Response(serializer.data, status=status.HTTP_200_OK)

        energy_usage = current_reading.reading - previous_reading.reading
        total_amount = energy_usage * meter_type.price
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(
            user=self.request.user,
            meter_type=meter_type,
            previous_reading=previous_reading,
            current_reading=current_reading,
            energy_usage=energy_usage,
            unit_price=meter_type.price,
            total_amount=total_amount,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StandardPaymentListCreateView(ListCreateAPIView):
    """
        get:
            Get authorization user's list of standard payment
            or
            get all list of payments if user.is_staff == True
        post:
            Create new payment
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = StandardPaymentSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return StandardPaymentModel.objects.all()
        return StandardPaymentModel.objects.filter(user_id=self.request.user.id)

    def post(self, request, *args, **kwargs):
        current_date = datetime.now()
        standard_meter_type = StandardMeterTypeModel.objects.all()
        for meter in standard_meter_type:
            payment = StandardPaymentModel.objects.filter(user_id=self.request.user.id,
                                                          standard_meter_type_id=meter.id).first()

            if payment and \
                    (current_date.month != payment.created_at.month or
                     (current_date.month == payment.created_at.month and current_date.year != payment.created_at.year)):
                print(payment and
                      (current_date.month != payment.created_at.month or
                       current_date.month == payment.created_at.month and current_date.year == payment.created_at.year))

                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)

                serializer.save(
                    user=self.request.user,
                    standard_meter_type=meter,
                )
        return Response(status=status.HTTP_201_CREATED)
