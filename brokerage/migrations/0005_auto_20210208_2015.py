# Generated by Django 3.1.3 on 2021-02-09 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokerage', '0004_auto_20201117_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker',
            name='account_number',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='broker',
            name='last_synced',
            field=models.DateField(null=True),
        ),
    ]