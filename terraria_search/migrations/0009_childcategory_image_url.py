# Generated by Django 3.2 on 2021-07-03 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terraria_search', '0008_auto_20210702_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='childcategory',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]