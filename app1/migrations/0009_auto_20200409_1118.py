# Generated by Django 3.0.4 on 2020-04-09 11:18

import autoslug.fields
from django.db import migrations


def generate_slug_and_order(apps, schema_editor):
    Project = apps.get_model('app1', 'SwModels')
    for i, obj in enumerate(Project.objects.all(), start=1):
        obj.url = '{}_{}'.format(obj.slug, i)
        obj.order = i
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20200409_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swmodels',
            name='url',
            field=autoslug.fields.AutoSlugField(
                always_update=True, editable=False, populate_from='name', unique=True),
        ),
    ]
