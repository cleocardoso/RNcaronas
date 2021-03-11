from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task
from datetime import datetime
from mail_templated import EmailMessage

@shared_task
def horario():
    print("--- Horário: ", datetime.now())


@shared_task(autoretry_for=(Exception,),retry_backoff=True,max_retries=None)
def enviarEmailCadastro(nome,email):

    message = EmailMessage('email/template_email.html', {'usuario': nome},
                           'cleotads21@gmail.com', to=[email])
    message.send()




@shared_task(autoretry_for=(Exception,),retry_backoff=True,max_retries=None)
def enviarEmail():
    print("Teste")



@periodic_task(
    run_every=(crontab(minute='*/10')),
    name="celery_test",
    ignore_result=True
)
def teste():
    print("***********************")