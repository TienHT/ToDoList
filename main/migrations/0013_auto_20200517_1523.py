# Generated by Django 3.0.5 on 2020-05-17 08:23

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200517_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='todo',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Todo'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_time',
            field=models.DateField(default=datetime.datetime(2020, 5, 17, 8, 23, 34, 414155, tzinfo=utc)),
        ),
    ]
