# Generated by Django 3.0.7 on 2020-12-31 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_aboutus'),
    ]

    operations = [
        migrations.AddField(
            model_name='openhours',
            name='markedClosed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]