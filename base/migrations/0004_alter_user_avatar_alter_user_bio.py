# Generated by Django 4.1.5 on 2023-01-07 10:06

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(default='images/default.jpg', max_length=255, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
