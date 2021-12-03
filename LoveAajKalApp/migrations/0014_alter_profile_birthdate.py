# Generated by Django 3.2.8 on 2021-11-30 01:34

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoveAajKalApp', '0013_alter_profile_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(default=datetime.date(1900, 1, 1), validators=[django.core.validators.MinValueValidator(datetime.date(1900, 1, 1)), django.core.validators.MaxValueValidator(datetime.date(2003, 11, 29))]),
        ),
    ]
