# Generated by Django 3.0.8 on 2020-07-23 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200723_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='date',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_type',
        ),
        migrations.AddField(
            model_name='service',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 23, 12, 15, 55, 117256)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 23, 12, 16, 12, 440172)),
            preserve_default=False,
        ),
    ]
