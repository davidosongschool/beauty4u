# Generated by Django 3.0.7 on 2020-12-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_auto_20201230_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitestats',
            name='day',
            field=models.CharField(blank=True, editable=False, max_length=10, null=True),
        ),
    ]
