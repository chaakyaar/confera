# Generated by Django 4.1.5 on 2023-04-23 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_person_usertype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='password',
            new_name='ph_no',
        ),
    ]
