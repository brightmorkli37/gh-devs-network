# Generated by Django 4.0.3 on 2022-03-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_address_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_website',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
