from datetime import datetime
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


UserModel = get_user_model()


class Note(models.Model):
    description = models.TextField()

    emotion = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    date = models.DateTimeField(
        default=datetime.now()
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Question(models.Model):
    question = models.TextField()

    def __str__(self):
        return f"{self.question}"
