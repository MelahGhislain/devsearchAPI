# Generated by Django 3.2.7 on 2021-09-10 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_rename_location_profile_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='adress',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
