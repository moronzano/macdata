# Generated by Django 3.0.4 on 2020-03-30 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_macdhcp'),
    ]

    operations = [
        migrations.AddField(
            model_name='macdhcp',
            name='dns_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='DNS'),
        ),
        migrations.AddField(
            model_name='macdhcp',
            name='ip_add',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
        migrations.AddField(
            model_name='macdhcp',
            name='ip_switch',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
        migrations.AddField(
            model_name='macdhcp',
            name='lastupd',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='macdhcp',
            name='mac',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Mac'),
        ),
        migrations.AddField(
            model_name='macdhcp',
            name='port',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Порт'),
        ),
        migrations.AddField(
            model_name='macdhcp',
            name='vlan',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Vlan'),
        ),
    ]
