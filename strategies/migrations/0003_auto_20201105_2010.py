# Generated by Django 3.1.3 on 2020-11-06 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('strategies', '0002_auto_20201105_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicoption',
            name='close_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='basicoption',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategies.account'),
        ),
    ]