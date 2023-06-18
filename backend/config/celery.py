import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('configs')

app.config_from_object('django.conf.settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send_reminder": {
        "task": "core.services.email_service.submission_reminder",
        "schedule": crontab(minute='5', hour='10')
    }
}
