# Generated by Django 3.0.7 on 2020-12-30 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_auto_20201230_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitestats',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
