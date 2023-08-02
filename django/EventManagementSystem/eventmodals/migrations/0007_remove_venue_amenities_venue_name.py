# Generated by Django 4.0.6 on 2023-07-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmodals', '0006_remove_event_location_event_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='amenities',
        ),
        migrations.AddField(
            model_name='venue',
            name='name',
            field=models.CharField(default='HVG', max_length=200),
        ),
    ]