# Generated by Django 2.2.1 on 2019-07-27 10:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fb_post_v2', '0007_auto_20190727_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='uuid',
            field=models.UUIDField(auto_created=uuid.UUID('d75d7c2c-8bec-41a6-8f31-571cf13270d5'), unique=True),
        ),
    ]
