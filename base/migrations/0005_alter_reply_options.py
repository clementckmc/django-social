# Generated by Django 4.1.5 on 2023-01-06 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_reply_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['created']},
        ),
    ]
