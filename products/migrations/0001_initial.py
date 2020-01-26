# Generated by Django 2.1.14 on 2020-01-26 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('productprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('productweight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('productdescription', models.TextField(max_length=300)),
                ('productimage', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('productupdatedate', models.DateTimeField(auto_now_add=True)),
                ('productstockqty', models.IntegerField()),
                ('productlive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.TextField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='productcategoryid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductCategories'),
        ),
    ]
