# Generated by Django 3.0.6 on 2020-05-21 14:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200517_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(default='Daily Activities', max_length=255),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_time',
            field=models.DateField(default=datetime.datetime(2020, 5, 21, 14, 21, 1, 294780, tzinfo=utc)),
        ),
    ]
