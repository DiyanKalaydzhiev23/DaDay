# Generated by Django 4.0.3 on 2022-04-27 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0006_remove_profile_parent_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadayuser',
            name='parent_email',
        ),
        migrations.AddField(
            model_name='profile',
            name='parent_email',
            field=models.EmailField(default=2002, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_sent_email',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 16, 21, 48, 381864)),
        ),
    ]
