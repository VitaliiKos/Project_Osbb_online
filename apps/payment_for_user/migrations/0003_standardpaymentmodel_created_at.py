# Generated by Django 4.2.1 on 2023-06-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_for_user', '0002_standardpaymentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpaymentmodel',
            name='created_at',
            field=models.DateTimeField(default='2023-03-09 13:27:56.656000'),
            preserve_default=False,
        ),
    ]
