# Generated by Django 3.1.3 on 2020-11-06 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicoption',
            name='fees',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='basicoption',
            name='premium',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='basicoption',
            name='stock_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='basicoption',
            name='strike',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
