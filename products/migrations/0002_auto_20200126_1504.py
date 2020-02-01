# Generated by Django 2.1.14 on 2020-01-26 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productcategoryid',
            new_name='product_category_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productdescription',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productimage',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productlive',
            new_name='product_live',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productname',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productprice',
            new_name='product_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productstockqty',
            new_name='product_stock_qty',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productupdatedate',
            new_name='product_update_date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productweight',
            new_name='product_weight',
        ),
        migrations.RenameField(
            model_name='productcategories',
            old_name='categoryname',
            new_name='category_name',
        ),
    ]