# Generated by Django 4.0.6 on 2023-07-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmodals', '0005_rename_name_registration_username_registration_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ManyToManyField(related_name='events', to='eventmodals.venue'),
        ),
    ]
