

from django.db import migrations, models
import uuid

# Generated by Django 2.2.1 on 2019-07-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb_post_v2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('uuid', models.UUIDField(default=uuid.UUID('27bbc664-d27c-46b9-a34d-bdb79217419b'), unique=True)),

                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]
