# Generated by Django 3.0.7 on 2021-01-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210102_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openhours',
            name='markedClosed',
            field=models.BooleanField(default=False),
        ),
    ]
