from django.db import models

from django.contrib.auth.models import User

# Create your models here.
#
# UserData Model for additional attributes necessary to User Model
class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=10, default='')
    USER_ROLE = [
        ('seller', 'Seller'),
        ('customer', 'Customer'),
    ]
    role = models.CharField(max_length=20, choices=USER_ROLE, blank=True, null=True)

    def __str__(self):
        return self.middlename