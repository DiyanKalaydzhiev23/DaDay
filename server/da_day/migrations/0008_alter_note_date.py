# Generated by Django 4.0.3 on 2022-04-02 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da_day', '0007_alter_note_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 3, 0, 8, 18, 683073)),
        ),
    ]
