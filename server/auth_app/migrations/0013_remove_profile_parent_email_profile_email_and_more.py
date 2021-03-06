# Generated by Django 4.0.3 on 2022-05-09 13:57

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0012_profile_image_alter_profile_last_sent_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='parent_email',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=2002, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=8),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_sent_email',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 9, 16, 57, 3, 980803)),
        ),
    ]
