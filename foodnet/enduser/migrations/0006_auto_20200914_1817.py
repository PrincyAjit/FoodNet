# Generated by Django 3.0.8 on 2020-09-14 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enduser', '0005_enduser_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enduser',
            name='enduser_city',
        ),
        migrations.RemoveField(
            model_name='enduser',
            name='enduser_country',
        ),
        migrations.RemoveField(
            model_name='enduser',
            name='enduser_state',
        ),
    ]