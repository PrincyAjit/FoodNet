# Generated by Django 3.0.8 on 2020-09-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enduser', '0008_enduser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduser',
            name='enduser_password',
            field=models.CharField(max_length=100),
        ),
    ]
