import datetime

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    end_data_pay = models.DateField(default=datetime.date.today() + datetime.timedelta(365), null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

