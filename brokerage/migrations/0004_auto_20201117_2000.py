# Generated by Django 3.1.3 on 2020-11-18 04:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokerage', '0003_broker_broker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker',
            name='open_date',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
    ]
