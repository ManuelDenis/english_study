# Generated by Django 2.2 on 2022-08-08 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_userprofile_end_data_pay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='stripe_customer_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='stripe_subscription_id',
        ),
    ]