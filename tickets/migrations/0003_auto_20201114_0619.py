# Generated by Django 3.0 on 2020-11-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20201114_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicleroute',
            name='routefrom',
        ),
        migrations.RemoveField(
            model_name='vehicleroute',
            name='routeto',
        ),
        migrations.AddField(
            model_name='vehicleroute',
            name='route',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
