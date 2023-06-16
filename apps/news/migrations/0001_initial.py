# Generated by Django 4.2.1 on 2023-06-07 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'news_comments',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9А-ЯҐЄІЇа-яєії -]{2,50}$', 'only letters min 2 max 50 ch')])),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'news_list',
                'ordering': ('-created_at',),
            },
        ),
    ]
