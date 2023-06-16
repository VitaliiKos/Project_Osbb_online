# Generated by Django 4.2.1 on 2023-06-07 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0003_rename_meterreadingsphotomodel_meterphotomodel'),
        ('readings', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterreadingsmodel',
            name='meter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reading', to='meter.metermodel'),
        ),
    ]