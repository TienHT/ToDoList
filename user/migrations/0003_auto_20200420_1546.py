# Generated by Django 3.0.5 on 2020-04-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200420_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='Unknown', max_length=255, unique=True),
        ),
    ]