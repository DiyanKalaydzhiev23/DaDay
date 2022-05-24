from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models


UserModel = get_user_model()


class Room(models.Model):
    room_name = models.CharField(
        unique=True,
        max_length=1000,
    )


class Message(models.Model):
    time_sent = models.DateTimeField(
        default=timezone.now,
    )

    read = models.BooleanField(
        default=False,
    )

    sender = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    room_name = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
    )


class TextMessage(Message):
    def __init__(self):
        super().__init__()

    message = models.CharField(
        max_length=1000,
    )
