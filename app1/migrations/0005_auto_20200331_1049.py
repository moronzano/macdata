# Generated by Django 3.0.4 on 2020-03-31 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20200330_0802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dhcptable',
            options={'ordering': ['ip_add'], 'verbose_name': 'DNS адрес', 'verbose_name_plural': 'DNS адреса'},
        ),
    ]
