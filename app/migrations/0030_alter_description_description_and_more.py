# Generated by Django 5.0.3 on 2024-03-26 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_description_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='description',
            field=models.TextField(default='النص باللغه العربية'),
        ),
        migrations.AlterField(
            model_name='description',
            name='description_en',
            field=models.TextField(default='النص باللغه الانجليزية'),
        ),
        migrations.AlterField(
            model_name='description',
            name='title',
            field=models.CharField(default='العنوان باللغة العربية', max_length=100),
        ),
        migrations.AlterField(
            model_name='description',
            name='title_en',
            field=models.CharField(default='العنوان باللغه الانجليزية', max_length=100),
        ),
    ]
