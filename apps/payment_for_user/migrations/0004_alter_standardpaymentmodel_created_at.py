# Generated by Django 4.2.1 on 2023-06-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_for_user', '0003_standardpaymentmodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardpaymentmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
