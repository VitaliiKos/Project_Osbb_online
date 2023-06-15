from rest_framework.serializers import ModelSerializer

from .models import MainUsersPaymentModel, PaymentModel


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = (
            'id', 'previous_reading', 'current_reading', 'energy_usage', 'unit_price', 'total_amount', 'user',
            'created_at', 'meter_type')
        read_only_fields = (
        'user', 'previous_reading', 'current_reading', 'energy_usage', 'unit_price', 'total_amount', 'meter_type')


class MainUsersPaymentSerializer(ModelSerializer):
    electricity_payment = PaymentSerializer()
    gas_payment = PaymentSerializer()
    water_payment = PaymentSerializer()

    class Meta:
        model = MainUsersPaymentModel
        fields = ('id', 'electricity_payment', 'gas_payment', 'water_payment', 'user', 'created_at')
        read_only_fields = ('user',)
