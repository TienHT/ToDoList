# Generated by Django 3.0.6 on 2020-05-24 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20200524_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(default='default-picture.png', upload_to='static/media/'),
        ),
    ]