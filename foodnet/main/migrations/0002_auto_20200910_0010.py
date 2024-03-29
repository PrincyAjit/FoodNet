# Generated by Django 3.0.8 on 2020-09-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalrecipe',
            name='video',
        ),
        migrations.AlterField(
            model_name='appliance',
            name='appliance_image',
            field=models.ImageField(upload_to='main_images/'),
        ),
        migrations.AlterField(
            model_name='generalrecipe',
            name='image',
            field=models.ImageField(upload_to='main_images/'),
        ),
        migrations.AlterField(
            model_name='generalrecipe',
            name='veg_nonveg',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='recipecategory',
            name='category_image',
            field=models.ImageField(default=None, upload_to='main_images/'),
        ),
    ]
