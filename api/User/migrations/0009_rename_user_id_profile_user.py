# Generated by Django 3.2.7 on 2021-09-10 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_alter_profile_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]