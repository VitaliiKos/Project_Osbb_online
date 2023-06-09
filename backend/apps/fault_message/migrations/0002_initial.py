# Generated by Django 4.2.1 on 2023-06-07 14:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fault_message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faultmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='faultcommentmodel',
            name='fault_msg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='fault_message.faultmodel'),
        ),
        migrations.AddField(
            model_name='faultcommentmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
