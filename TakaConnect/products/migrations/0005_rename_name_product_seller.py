# Generated by Django 4.2.6 on 2023-10-18 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_sellername_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='seller',
        ),
    ]