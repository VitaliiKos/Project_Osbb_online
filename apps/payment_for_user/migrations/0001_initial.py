# Generated by Django 4.2.1 on 2023-06-09 13:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('readings', '0003_alter_meterreadingsmodel_meter'),
        ('meter', '0006_alter_metertypemodel_specify'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy_usage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_price', models.FloatField(default=5.0)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('previous_reading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='previous_payment', to='readings.meterreadingsmodel')),
                ('current_reading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_payment', to='readings.meterreadingsmodel')),
                ('meter_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='meter.metertypemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'payment',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='MainUsersPaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('electricity_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electricity_payment', to='payment_for_user.paymentmodel')),
                ('gas_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gas_payment', to='payment_for_user.paymentmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('water_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water_payment', to='payment_for_user.paymentmodel')),
            ],
            options={
                'db_table': 'main_users_payment',
                'ordering': ('-created_at',),
            },
        ),
    ]