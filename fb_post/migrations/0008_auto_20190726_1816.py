# Generated by Django 2.2.1 on 2019-07-26 18:16
import uuid

from django.db import migrations

def gen_uuid(apps, schema_editor):
    Person = apps.get_model('fb_post', 'Person')
    for row in Person.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=['uuid'])

class Migration(migrations.Migration):

    dependencies = [
        ('fb_post', '0007_auto_20190726_1816'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop)
    ]
