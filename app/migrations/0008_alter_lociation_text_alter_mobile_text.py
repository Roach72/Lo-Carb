# Generated by Django 5.0.3 on 2024-03-17 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_lociation_rename_whatsapplink_whatsappchat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lociation',
            name='text',
            field=models.CharField(default='Location Link', max_length=100),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='text',
            field=models.CharField(default='Mobile Link', max_length=100),
        ),
    ]
