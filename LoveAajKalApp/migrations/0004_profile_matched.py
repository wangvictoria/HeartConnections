# Generated by Django 3.2.8 on 2021-11-05 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoveAajKalApp', '0003_auto_20211105_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='matched',
            field=models.BooleanField(default=False),
        ),
    ]
