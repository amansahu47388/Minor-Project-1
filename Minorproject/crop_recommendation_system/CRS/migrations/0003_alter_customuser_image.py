# Generated by Django 3.2.25 on 2024-10-20 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0002_auto_20241020_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
