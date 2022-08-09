from django.contrib import admin
from payments.models import Product, Price, UserProfile


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'stripe_product_id']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'stripe_price_id', 'price']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'end_data_pay']
