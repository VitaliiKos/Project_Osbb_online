# Generated by Django 4.2.1 on 2023-06-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0005_alter_metertypemodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metertypemodel',
            name='specify',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
