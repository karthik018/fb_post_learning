# Generated by Django 2.2.1 on 2019-07-26 18:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fb_post', '0006_person_person_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person_id',
            field=models.UUIDField(default=uuid.UUID(
                'e26bab62-24ac-4d06-9fcd-c1dc521b203a'), null=True),
        ),
    ]