# Generated by Django 4.1.5 on 2023-04-23 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_venue_photo_conference_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='usertype',
        ),
    ]
