# Generated by Django 3.0.8 on 2020-07-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='status',
            field=models.IntegerField(choices=[(1, 'AVAILABLE'), (2, 'BLOCKED'), (3, 'BOOKED')], default=1),
        ),
    ]
