from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import models as auth_models
from server.auth_app.managers import DaDayUserManager


class DaDayUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(
        max_length=25,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = DaDayUserManager()


class Profile(models.Model):
    parent_email = models.EmailField()

    avatar = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    last_sent_email = models.DateTimeField(
        default=datetime.now()
    )

    user = models.OneToOneField(
        DaDayUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
