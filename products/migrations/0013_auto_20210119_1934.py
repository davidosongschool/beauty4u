# Generated by Django 3.1.4 on 2021-01-19 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='added_by',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
