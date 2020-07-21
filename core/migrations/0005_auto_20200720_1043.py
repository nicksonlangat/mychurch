# Generated by Django 3.0.8 on 2020-07-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_seat_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='live',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='seat',
            name='status',
            field=models.IntegerField(choices=[(1, 'Available'), (2, 'Blocked'), (3, 'Booked')], default=1),
        ),
    ]