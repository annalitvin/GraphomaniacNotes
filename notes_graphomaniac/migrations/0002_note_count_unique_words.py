# Generated by Django 2.0.4 on 2018-06-06 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_graphomaniac', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='count_unique_words',
            field=models.IntegerField(default=0),
        ),
    ]