# Generated by Django 3.0.7 on 2020-12-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_sitesettings_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
    ]