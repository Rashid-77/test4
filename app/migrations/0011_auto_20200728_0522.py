# Generated by Django 2.2.14 on 2020-07-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200728_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image_path',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]