# Generated by Django 2.2.13 on 2020-08-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200820_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(default='no_image_available-1.png', upload_to='', verbose_name='Main image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]