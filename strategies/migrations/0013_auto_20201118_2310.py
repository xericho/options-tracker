# Generated by Django 3.1.3 on 2020-11-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategies', '0012_auto_20201118_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicoption',
            name='close_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='basicoption',
            name='fees',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='basicoption',
            name='profitloss',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='spreadoption',
            name='close_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='spreadoption',
            name='fees',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='spreadoption',
            name='profitloss',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]