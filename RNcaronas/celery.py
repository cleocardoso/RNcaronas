from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RNcaronas.settings')
app = Celery('RNcaronas',broker='redis://localhost:6379/0')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

from tasks.task import enviarEmailCadastro



#Comando para rodar
# celery -A RNcaronas worker -l info
# celery -A RNcaronas  beat -l info
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.timezone = 'UTC'