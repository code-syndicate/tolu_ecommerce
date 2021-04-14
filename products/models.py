import uuid
from django.db import models

# helper funcs


def handle_upload_1(instance, filename):
    return "{0}/{1}".format(instance.category_name, filename)


def handle_upload_2(instance, filename):
    return "{0}/{1}/{2}".format(instance.category.category_name, instance.product_name, filename)


# Products Model
class Product(models.Model):
    product_name = models.CharField(max_length=128, blank=False, )
    sku = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    category = models.ForeignKey(
        "ProductCategory", related_name='products', on_delete=models.CASCADE)
    price_per_unit = models.DecimalField(
        default=5000, decimal_places=2, max_digits=11)
    amount_in_stock = models.PositiveIntegerField(default=15)
    slash_percentage = models.PositiveIntegerField(max_length=2, default=5)
    picture = models.ImageField(max_length=255, upload_to=handle_upload_2)

    @property
    def price(self):
        return round(float(self.price_per_unit) * ((100-self.slash_percentage)/100), 2)

    def __str__(self):
        return self.product_name


# Product category
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=64, blank=False, unique=True)
    cover_picture = models.ImageField(
        max_length=255, upload_to=handle_upload_1)

    def __str__(self):
        return self.category_name
