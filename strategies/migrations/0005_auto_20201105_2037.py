# Generated by Django 3.1.3 on 2020-11-06 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brokerage', '0001_initial'),
        ('strategies', '0004_auto_20201105_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicoption',
            name='brokerage',
        ),
        migrations.AddField(
            model_name='basicoption',
            name='broker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='brokerage.broker'),
        ),
        migrations.DeleteModel(
            name='Brokerage',
        ),
    ]
