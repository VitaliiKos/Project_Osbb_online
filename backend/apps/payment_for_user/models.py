from django.contrib.auth import get_user_model
from django.db import models

from apps.meter.models import MeterModel, MeterTypeModel, StandardMeterTypeModel
from apps.readings.managers import StandardMeterPymentManager
from apps.readings.models import MeterReadingsModel
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class StandardPaymentModel(models.Model):
    """
    Receipt generation for standard service
    """

    class Meta:
        db_table = 'standard_payment'
        ordering = ('-created_at',)

    standard_meter_type = models.ForeignKey(StandardMeterTypeModel, on_delete=models.CASCADE,
                                            related_name='standard_payment')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = StandardMeterPymentManager.as_manager()


class PaymentModel(models.Model):
    """
    Receipt generation for each service
    """

    class Meta:
        db_table = 'payment'
        ordering = ('-created_at',)

    meter_type = models.ForeignKey(MeterTypeModel, on_delete=models.CASCADE, related_name='payment')
    previous_reading = models.ForeignKey(MeterReadingsModel, on_delete=models.CASCADE, related_name='previous_payment')
    current_reading = models.ForeignKey(MeterReadingsModel, on_delete=models.CASCADE, related_name='current_payment')
    energy_usage = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.FloatField(default=5.0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class MainUsersPaymentModel(models.Model):
    class Meta:
        db_table = 'main_users_payment'
        ordering = ('-created_at',)

    electricity_payment = models.ForeignKey(PaymentModel, on_delete=models.CASCADE, related_name='electricity_payment')
    gas_payment = models.ForeignKey(PaymentModel, on_delete=models.CASCADE, related_name='gas_payment')
    water_payment = models.ForeignKey(PaymentModel, on_delete=models.CASCADE, related_name='water_payment')
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
