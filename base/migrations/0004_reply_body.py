# Generated by Django 4.1.5 on 2023-01-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_reply_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
