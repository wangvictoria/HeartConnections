# Generated by Django 3.2.8 on 2021-11-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoveAajKalApp', '0006_alter_profile_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='matched_with',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='notes',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]