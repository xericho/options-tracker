# Generated by Django 3.1.3 on 2021-02-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategies', '0015_auto_20210208_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicoption',
            name='orderId',
        ),
        migrations.RemoveField(
            model_name='spreadoption',
            name='orderId',
        ),
        migrations.AddField(
            model_name='basicoption',
            name='order_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='spreadoption',
            name='order_id',
            field=models.CharField(max_length=15, null=True),
        ),
    ]