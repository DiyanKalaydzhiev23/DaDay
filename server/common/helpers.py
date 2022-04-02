from django.core.mail import send_mail
from django.http import HttpResponse

from server import settings


def my_mail(request=None, email=None):
    if request:
        subject = "Registration greetings"
    else:
        subject = "else"

    msg = "We are pleasured to see that you choose DaDay for personal diary for your child. " \
            "We can ensure you that we will deliver the best possible experience for your beloved one " \
            "and give you monthly reports on their mental health status. " \
            "" \
            "Regards," \
            "AllowCookiesTeam"

    to = email
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

    if res == 1:
        msg = "Mail Sent Successfully."
    else:
        msg = "Mail Sending Failed."

    return HttpResponse(msg)


