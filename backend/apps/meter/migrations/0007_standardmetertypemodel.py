# Generated by Django 4.2.1 on 2023-06-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0006_alter_metertypemodel_specify'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardMeterTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specify', models.CharField(max_length=150, unique=True)),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'standard_meter_type',
            },
        ),
    ]
