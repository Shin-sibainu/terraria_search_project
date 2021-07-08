# Generated by Django 3.2 on 2021-07-07 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terraria_search', '0013_alter_items_how_to_get'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='needed_material',
        ),
        migrations.RemoveField(
            model_name='items',
            name='needed_material_image_url',
        ),
        migrations.RemoveField(
            model_name='items',
            name='workplace',
        ),
        migrations.RemoveField(
            model_name='items',
            name='workplace_image_url',
        ),
        migrations.AddField(
            model_name='items',
            name='item_needed_material',
            field=models.ManyToManyField(null=True, related_name='_terraria_search_items_item_needed_material_+', to='terraria_search.Items'),
        ),
        migrations.AddField(
            model_name='items',
            name='item_workplace',
            field=models.ManyToManyField(null=True, related_name='_terraria_search_items_item_workplace_+', to='terraria_search.Items'),
        ),
    ]