from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



from django.core import mail
from django.conf import settings
from celery import shared_task
from mail_templated import EmailMessage

@shared_task(autoretry_for=(Exception,),retry_backoff=True,max_retries=None)
def sendTemplate(message, emails):

    message = EmailMessage('email/email.html', message,
                           settings.EMAIL_HOST_USER, to=[emails])
    message.send()

@shared_task(autoretry_for=(Exception,),retry_backoff=True,max_retries=None)
def send(title, message, emails):
    connection = mail.get_connection()
    print(connection)
    connection.open()
    mail.send_mail(title,
                   message,
                   settings.EMAIL_HOST_USER,
                   [emails],
                   fail_silently=False)
    connection.close()




