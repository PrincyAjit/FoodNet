# Generated by Django 3.0.8 on 2020-09-14 09:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0005_auto_20200910_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
