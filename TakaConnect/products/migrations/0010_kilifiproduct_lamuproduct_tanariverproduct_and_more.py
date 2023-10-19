# Generated by Django 4.2.6 on 2023-10-18 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_mombasaproduct_kwaleproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='KilifiProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('contact', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.category')),
                ('categorytype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.categorytype')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.location')),
            ],
        ),
        migrations.CreateModel(
            name='LamuProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('contact', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.category')),
                ('categorytype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.categorytype')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.location')),
            ],
        ),
        migrations.CreateModel(
            name='TanaRiverProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('contact', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.category')),
                ('categorytype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.categorytype')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.location')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]