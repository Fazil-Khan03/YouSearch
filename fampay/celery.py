from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fampay.settings')

app = Celery('fampay')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-15-seconds' : {
        'task': 'api.tasks.call_google_api',
        'schedule':15,
    }
}

@app.task(bind=True)
def debug_task(self):
    print('request---->')
