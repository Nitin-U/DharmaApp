from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#
# Product Model for Items to buy/sell
class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=144)
    PRODUCT_TYPE_CHOICES = [
        ('', '--- Your Product Falls Under Which Type? ---'),
        ('Package', 'Package'),
        ('Product', 'Product'),
    ]
    product_type = models.CharField(max_length=144, choices=PRODUCT_TYPE_CHOICES)
    PRODUCT_CATEGORY_CHOICES = [
        ('', '--- Your Product Falls Under Which Type? ---'),
        ('Category1', 'Category1'),
        ('Category2', 'Category2'),
        ('Category3', 'Category3'),
        ('Category4', 'Category4'),
        ('Category5', 'Category5'),
    ]
    product_category = models.TextField(max_length=144, choices=PRODUCT_CATEGORY_CHOICES)
    product_description = models.CharField(max_length=144)
    product_quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock = models.BooleanField()

    def __str__(self):
        return self.product_name