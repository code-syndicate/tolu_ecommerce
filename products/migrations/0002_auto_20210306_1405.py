# Generated by Django 3.1.6 on 2021-03-06 13:05

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slash_percentage',
            field=models.PositiveIntegerField(default=5, max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(max_length=255, upload_to=products.models.handle_upload_2),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='cover_picture',
            field=models.ImageField(max_length=255, upload_to=products.models.handle_upload_1),
        ),
    ]
