# Generated by Django 3.0.3 on 2020-11-05 11:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_class_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='updated',
            field=models.DateField(default=datetime.datetime(2020, 11, 5, 11, 17, 7, 330795, tzinfo=utc)),
        ),
    ]
