import os

from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы успешно зарегистрированы на note-app',
        'Мы будем присылать сообщения о важных событиях',
        os.getenv('ADMIN_EMAIL'),
        [user_email],
        fail_silently=False,
    )
