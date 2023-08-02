# Generated by Django 4.0.6 on 2023-07-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmodals', '0003_event_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='is_accepted',
            new_name='is_payed',
        ),
        migrations.AddField(
            model_name='registration',
            name='name',
            field=models.CharField(default='none', max_length=100),
        ),
    ]