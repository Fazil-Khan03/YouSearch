from celery import shared_task
from fampay.celery import app
from django.contrib.auth.models import User
from .script import fetch_videos
@shared_task
def call_google_api():
    fetch_videos()
    



    
 


