# Generated by Django 3.0.5 on 2020-04-21 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200420_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='Tên Đăng Nhập'),
        ),
    ]
