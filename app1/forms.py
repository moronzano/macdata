from django import forms
#from django.forms import ModelForm
from django.db import models
from .models import Switches, SwModels


class SwitchesForm(forms.ModelForm):
    class Meta:
        model = Switches
        fields = ['ip_switch', 'name', 'lastupd', 'rem',
                  'corp', 'etag', 'room', 'uplink', 'livedate', 'need']
    name = forms.ModelChoiceField(
        queryset=SwModels.objects.all(), label="Модель", empty_label=None)
    ip_switch = forms.CharField(max_length=39, label="ip address")
    lastupd = forms.DateTimeField(label="Попытка связи")
    rem = forms.CharField(max_length=10, label="Доступ")
    corp = forms.CharField(max_length=50, label="Корпус")
    etag = forms.CharField(max_length=50, label="Этаж")
    room = forms.CharField(max_length=50, label="Кабинет")
    uplink = forms.CharField(max_length=50, label="Входящий порт")
    livedate = forms.DateTimeField(label="Последний доступ")
    need = forms.CharField(max_length=1, label="Актуальность")
