# Generated by Django 2.0.4 on 2018-05-28 20:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180528_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
