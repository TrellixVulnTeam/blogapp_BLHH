# Generated by Django 2.2.7 on 2019-12-14 19:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0008_auto_20191213_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 14, 19, 37, 22, 202502, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='candidate',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 14, 19, 37, 22, 202502, tzinfo=utc)),
        ),
    ]