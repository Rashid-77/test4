# Generated by Django 2.2.14 on 2020-07-28 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200724_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image_path',
            field=models.FilePathField(blank=True, default='default.png'),
        ),
        migrations.AlterField(
            model_name='supplierproduct',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=11, verbose_name='Price'),
        ),
    ]