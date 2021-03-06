# Generated by Django 3.1.4 on 2021-01-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210109_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured_product',
            field=models.BooleanField(choices=[(True, 'Yes, This is a featured product!'), (False, 'No')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(blank=True, choices=[(True, 'In Stock'), (False, 'Out of Stock!')], default=True, null=True),
        ),
    ]
