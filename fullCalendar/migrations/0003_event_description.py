# Generated by Django 4.2.13 on 2024-07-20 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullCalendar', '0002_alter_event_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]