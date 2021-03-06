# Generated by Django 2.0.6 on 2018-10-20 07:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0010_auto_20181020_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='prognosis',
            name='isVerified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(default=datetime.datetime(2018, 10, 20, 7, 1, 2, 168981, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='prognosis',
            name='startTime',
            field=models.DateField(default=datetime.datetime(2018, 10, 20, 7, 1, 2, 171122, tzinfo=utc)),
        ),
    ]
