# Generated by Django 3.2.25 on 2024-10-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0003_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
