# Generated by Django 3.0.8 on 2020-09-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200910_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalrecipe',
            name='recipe_slug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='recipecategory',
            name='category_slug',
            field=models.CharField(default=1, max_length=200, unique=True),
        ),
    ]
