# Generated by Django 4.1.5 on 2023-05-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_conference_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Time_and_Date',
        ),
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='ending_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='starting_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]
