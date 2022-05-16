
from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from server import settings
from random import choice
from time import sleep
from server.auth_app.models import ResetPasswordData, Profile

UserModel = get_user_model()


@shared_task
def send_greeting_email(email):
    subject = "Registration greetings"
    html_message = render_to_string('greeting_email.html')
    to = email
    res = send_mail(subject, '', settings.EMAIL_HOST_USER, [to], html_message=html_message)


@shared_task
def handle_reset_password(email):
    symbols = [
        '1', '2', '3', '4', '5',
        '6', '7', '8', '9', '$',
        'a', 'b', 'c', 'd', 'e',
        'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y',
        'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I',
        '-', '!', '(', ')', '%',
        'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '@', '#', '?',
    ]

    text = ''.join([choice(symbols) for _ in range(7)])

    token_data = ResetPasswordData(
        user_id=Profile.objects.get(email=email).user.id,
        token=text,
    )
    token_data.save()

    subject = "Reset Password - DaDay"
    html_message = render_to_string('password_reset_email.html', {'code': text})
    to = email

    send_mail(subject, '', settings.EMAIL_HOST_USER, [to], html_message=html_message)


@shared_task
def delete_reset_password_token(email):
    sleep(600)

    tokens = ResetPasswordData.objects.filter(user_id=Profile.objects.get(email=email).user.id)
    for token in tokens:
        token.delete()
