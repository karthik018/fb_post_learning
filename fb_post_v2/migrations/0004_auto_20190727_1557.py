# Generated by Django 2.2.1 on 2019-07-27 10:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fb_post_v2', '0003_auto_20190727_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('cd7958bf-c9e1-4b3f-8c89-1a811318b3cd'), unique=True),
        ),
    ]
