# Generated by Django 4.2.13 on 2024-07-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimony', '0003_testimonial_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
