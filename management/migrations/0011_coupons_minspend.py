# Generated by Django 3.0.7 on 2020-12-28 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_auto_20201227_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons',
            name='minspend',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
