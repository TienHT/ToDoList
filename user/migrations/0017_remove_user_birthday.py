# Generated by Django 3.0.6 on 2020-05-24 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20200524_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]
