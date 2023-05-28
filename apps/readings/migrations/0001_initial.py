# Generated by Django 4.2.1 on 2023-05-28 16:05

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import core.services.upload_reading_service


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeterReadingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading', models.IntegerField(validators=[django.core.validators.RegexValidator('^\\d{6}$', 'readings is 6 characters with no space')])),
                ('meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='meter.metermodel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'readings',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='MeterReadingsPhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to=core.services.upload_reading_service.upload_to)),
                ('meter_readings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='readings.meterreadingsmodel')),
            ],
            options={
                'db_table': 'meter_readings_photo',
                'ordering': ('id',),
            },
        ),
    ]
