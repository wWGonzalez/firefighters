# Generated by Django 2.0.4 on 2018-05-28 20:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
