# Generated by Django 2.2.13 on 2020-08-20 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(default='no_image_available-1.png', upload_to='')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='order')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Supplier name')),
                ('zip_code', models.CharField(default=None, max_length=6, verbose_name='zip code')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='product name')),
                ('vendor_id', models.CharField(default=None, max_length=50, unique=True, verbose_name='vendor code')),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=11, verbose_name='Price')),
                ('availability', models.BooleanField(default=False)),
                ('image', models.ManyToManyField(blank=True, related_name='products', to='app.Image')),
                ('supplier', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Supplier')),
            ],
        ),
    ]
