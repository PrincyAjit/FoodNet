# Generated by Django 3.0.8 on 2020-09-09 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('enduser', '0002_auto_20200910_0010'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EndUserFollowers',
            new_name='EndUserFollower',
        ),
    ]