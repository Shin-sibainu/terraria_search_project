# Generated by Django 3.2.4 on 2021-06-30 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terraria_search', '0005_auto_20210630_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentcategory',
            name='image',
            field=models.ImageField(blank=True, height_field=32, null=True, upload_to='images/', width_field=32),
        ),
    ]
