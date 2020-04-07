from django.db import models
from macaddress.fields import MACAddressField
from django.db import connection


class SwModels(models.Model):
    name = models.CharField("Модель коммутатора", max_length=20)
    part_n = models.CharField("Part No", max_length=20, null=True)
    description = models.CharField("Описание", max_length=20, null=True)
    #slug = models.SlugField(max_length=150, unique=True)

    # def get_absolute_url(self):
    #    return reverse('switch_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель коммутатора"
        verbose_name_plural = "Модели коммутаторов"


class Switches(models.Model):
    ip_switch = models.GenericIPAddressField(default='127.0.0.1')
    name = models.ForeignKey(
        SwModels, verbose_name="Модель коммутатора", on_delete=models.SET_NULL, null=True
    )
    lastupd = models.DateTimeField("Попытка связи", null=True, blank=True)
    rem = models.CharField("Доступ", max_length=10, default='no access')
    corp = models.CharField("Корпус", max_length=50, default='27')
    etag = models.CharField("Этаж", max_length=50, default='1')
    room = models.CharField("Кабинет", max_length=50, default='1')
    uplink = models.CharField("Входящий порт", max_length=50, default='24')
    livedate = models.DateTimeField("Последний доступ", null=True, blank=True)
    need = models.CharField("Актуальность", max_length=1, default='1')
    #slug = models.SlugField(max_length=150, unique=True)

    # def get_absolute_url(self):
    #    return reverse('macs_detail_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['ip_switch']
        verbose_name = "Коммутатор"
        verbose_name_plural = "Коммутаторы"

    def __str__(self):
        # return 'IP коммутатора {0}, Последняя связь {1}, Корпус {2}'.format(self.ip_switch, self.lastupd, self.corp)
        return self.ip_switch


class DhcpTable(models.Model):
    ip_add = models.GenericIPAddressField(default='127.0.0.1')
    mac = MACAddressField(null=True, blank=True)
    mac_txt = models.CharField("Mac txt", max_length=50, null=True, blank=True)
    dns_name = models.CharField(
        "DNS имя", max_length=50, null=True, blank=True)
    fl = models.IntegerField(default=1)

    class Meta:
        ordering = ['ip_add']
        verbose_name = "DNS адрес"
        verbose_name_plural = "DNS адреса"

    def __str__(self):
        return self.ip_add


class StoreMac(models.Model):
    ip_switch = models.ForeignKey(
        Switches, on_delete=models.SET_NULL, null=True)
    port = models.CharField("Порт", max_length=50, null=True, blank=True)
    mac = models.CharField("Mac адрес", max_length=50, null=True, blank=True)
    lastupd = models.DateTimeField("Дата", null=True, blank=True)
    vlan = models.CharField("Vlan", max_length=4, null=True, blank=True)
    nport = models.CharField("Need", max_length=1, null=True, blank=True)
    portview = models.CharField(
        "ComWare", max_length=50, null=True, blank=True)
    ip_switch2 = models.GenericIPAddressField(default='127.0.0.1')

    class Meta:
        ordering = ['ip_switch']
        verbose_name = "Mac адрес"
        verbose_name_plural = "Mac адреса"

    def __str__(self):
        return self.mac


class MacDhcp_Op(models.Manager):
    def Mac_to_Dhcp(self):

        cursor = connection.cursor()
        cursor.execute(""" SELECT s.ip_switch,t.port,t.mac, t.lastupd, t.ip_add,
        t.dns_name,t.vlan FROM app1_switches s inner join
        (select app1_storemac.ip_switch_id,app1_storemac.port,app1_storemac.mac,app1_storemac.lastupd,
        app1_dhcptable.ip_add, app1_dhcptable.dns_name, app1_storemac.vlan
        from app1_storemac inner join app1_dhcptable on
        app1_storemac.mac=app1_dhcptable.mac_txt) t on s.id=t.ip_switch_id
        order by s.ip_switch,t.port""")
        data = cursor.fetchall()
        return data


class MacDhcp(models.Model):
    objects = MacDhcp_Op()
