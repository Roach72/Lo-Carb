# Generated by Django 5.0.3 on 2024-03-21 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_socialmedialink_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lociation',
            name='image',
        ),
    ]