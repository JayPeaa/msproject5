# Generated by Django 2.1.14 on 2020-04-10 11:35

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200325_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
