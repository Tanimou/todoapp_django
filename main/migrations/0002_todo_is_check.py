# Generated by Django 3.2.9 on 2021-11-16 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_check',
            field=models.BooleanField(default='False'),
        ),
    ]
