# Generated by Django 3.1.3 on 2020-11-06 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='trading_exp',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Noob'), (2, 'Proficient'), (3, 'Experienced')], default=1),
        ),
    ]
