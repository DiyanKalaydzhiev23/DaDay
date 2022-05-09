from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import models as auth_models
from server.auth_app.managers import DaDayUserManager
from django.contrib.postgres.fields import ArrayField


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
    email = models.EmailField(
        unique=True,
    )

    image = models.ImageField(
        upload_to='images',
        default='images/default_image_qvmqoi.png',
    )

    avatar = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    last_sent_email = models.DateTimeField(
        default=datetime.now()
    )

    friends = ArrayField(
        models.IntegerField(),
        default=list,
        size=8,
    )

    pending_friend_requests = ArrayField(
        models.IntegerField(),
        default=list,
    )

    user = models.OneToOneField(
        DaDayUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class ResetPasswordData(models.Model):
    user_id = models.IntegerField()

    token = models.CharField(
        max_length=150
    )

    token_submit = models.BooleanField(
        default=False,
    )
