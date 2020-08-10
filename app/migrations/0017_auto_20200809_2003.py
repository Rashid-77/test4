# Generated by Django 2.2 on 2020-08-09 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200807_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(blank=True, default='no_image_available-1.png', upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='product name'),
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.Image'),
        ),
    ]
