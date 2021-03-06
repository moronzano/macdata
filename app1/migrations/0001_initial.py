# Generated by Django 3.0.4 on 2020-03-30 06:42

from django.db import migrations, models
import django.db.models.deletion
import macaddress.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DhcpTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_add', models.GenericIPAddressField(default='127.0.0.1')),
                ('mac', macaddress.fields.MACAddressField(blank=True, integer=True, null=True)),
                ('mac_txt', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mac txt')),
                ('dns_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='DNS имя')),
                ('fl', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'DNS адрес',
                'verbose_name_plural': 'DNS адреса',
            },
        ),
        migrations.CreateModel(
            name='SwModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Модель коммутатора')),
                ('part_n', models.CharField(max_length=20, null=True, verbose_name='Part No')),
                ('description', models.CharField(max_length=20, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель коммутатора',
                'verbose_name_plural': 'Модели коммутаторов',
            },
        ),
        migrations.CreateModel(
            name='Switches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_switch', models.GenericIPAddressField(default='127.0.0.1')),
                ('lastupd', models.DateTimeField(blank=True, null=True, verbose_name='Попытка связи')),
                ('rem', models.CharField(default='no access', max_length=10, verbose_name='Доступ')),
                ('corp', models.CharField(default='27', max_length=50, verbose_name='Корпус')),
                ('etag', models.CharField(default='1', max_length=50, verbose_name='Этаж')),
                ('room', models.CharField(default='1', max_length=50, verbose_name='Кабинет')),
                ('uplink', models.CharField(default='24', max_length=50, verbose_name='Входящий порт')),
                ('livedate', models.DateTimeField(blank=True, null=True, verbose_name='Последний доступ')),
                ('need', models.CharField(default='1', max_length=1, verbose_name='Актуальность')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.SwModels', verbose_name='Модель коммутатора')),
            ],
            options={
                'verbose_name': 'Коммутатор',
                'verbose_name_plural': 'Коммутаторы',
            },
        ),
        migrations.CreateModel(
            name='StoreMac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(blank=True, max_length=50, null=True, verbose_name='Порт')),
                ('mac', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mac адрес')),
                ('lastupd', models.DateTimeField(blank=True, null=True, verbose_name='Дата')),
                ('vlan', models.CharField(blank=True, max_length=4, null=True, verbose_name='Vlan')),
                ('nport', models.CharField(blank=True, max_length=1, null=True, verbose_name='Need')),
                ('portview', models.CharField(blank=True, max_length=50, null=True, verbose_name='ComWare')),
                ('ip_switch2', models.GenericIPAddressField(default='127.0.0.1')),
                ('ip_switch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.Switches')),
            ],
            options={
                'verbose_name': 'Mac адрес',
                'verbose_name_plural': 'Mac адреса',
                'ordering': ['ip_switch'],
            },
        ),
    ]
