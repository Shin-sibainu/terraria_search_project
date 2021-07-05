# Generated by Django 3.2 on 2021-07-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terraria_search', '0009_childcategory_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.ManyToManyField(null=True, related_name='item', to='terraria_search.Category'),
        ),
        migrations.AlterField(
            model_name='items',
            name='childcategory',
            field=models.ManyToManyField(null=True, related_name='item', to='terraria_search.ChildCategory'),
        ),
    ]
