# Generated by Django 3.0.8 on 2020-09-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enduser', '0006_auto_20200914_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduser',
            name='enduser_bio',
            field=models.TextField(default='-'),
        ),
    ]
