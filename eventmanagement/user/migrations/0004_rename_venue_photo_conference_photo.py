# Generated by Django 4.1.5 on 2023-03-14 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_conference_venue_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conference',
            old_name='venue_photo',
            new_name='photo',
        ),
    ]
