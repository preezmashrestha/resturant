# Generated by Django 5.0.1 on 2024-03-22 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='qty',
            new_name='qty_of_order',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='qty_total',
            new_name='qty_in_recipe',
        ),
    ]
