# Generated by Django 2.0.4 on 2018-06-07 04:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes_graphomaniac', '0003_auto_20180607_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
