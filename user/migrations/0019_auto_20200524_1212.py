# Generated by Django 3.0.6 on 2020-05-24 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
