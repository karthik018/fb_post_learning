# Generated by Django 2.2.1 on 2019-07-27 10:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fb_post_v2', '0005_auto_20190727_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='uuid',
            field=models.UUIDField(auto_created=uuid.UUID('cc27e4ef-3820-436f-8c76-6cc0221c047b'), unique=True),
        ),
    ]
