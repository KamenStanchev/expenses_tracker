# Generated by Django 4.0.5 on 2022-06-18 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0003_alter_profile_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_image',
            new_name='image',
        ),
    ]