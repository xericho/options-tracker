# Generated by Django 3.1.3 on 2020-11-07 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategies', '0006_auto_20201106_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicoption',
            name='close_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='basicoption',
            name='exp_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='basicoption',
            name='open_date',
            field=models.DateField(),
        ),
    ]
