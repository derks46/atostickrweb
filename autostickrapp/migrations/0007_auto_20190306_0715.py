# Generated by Django 2.0.10 on 2019-03-06 13:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('autostickrapp', '0006_auto_20190306_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 6, 13, 15, 4, 184335, tzinfo=utc)),
        ),
    ]