# Generated by Django 2.1.14 on 2020-03-10 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200307_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image_name',
            field=models.TextField(default='picture', max_length=200),
            preserve_default=False,
        ),
    ]
