from django.db import models

from django.contrib.auth.models import User

# Create your models here.
#
# UserData Model for additional attributes necessary to User Model
class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, default='')
    USER_CHOICES = [
        ('Cust', 'Customer'),
        ('Pack', 'Package Provider'),
        ('Prod', 'Product Seller'),
    ]
    role = models.CharField(max_length=20, choices=USER_CHOICES, default='')