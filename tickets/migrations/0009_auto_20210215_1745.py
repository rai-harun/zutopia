# Generated by Django 3.1.6 on 2021-02-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20201115_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vimage',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
