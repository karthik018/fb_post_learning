# Generated by Django 2.2.1 on 2019-07-27 10:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fb_post_v2', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('a405b1fc-16c8-4cb0-9dc1-390a2c56950c'), unique=True),
        ),
    ]
