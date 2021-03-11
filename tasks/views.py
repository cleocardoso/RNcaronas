from django.shortcuts import render

from celery.schedules import crontab
from celery.task import periodic_task





@periodic_task(
   run_every=(crontab(minute='*/1')),
   name="celery_test",
   ignore_result=True
)
def teste():
    print("TEST")
