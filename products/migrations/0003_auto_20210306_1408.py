# Generated by Django 3.1.6 on 2021-03-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210306_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_per_unit',
            field=models.DecimalField(decimal_places=2, default=5000, max_digits=11),
        ),
    ]