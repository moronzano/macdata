from django import forms
#from django.forms import ModelForm
from django.db import models
from .models import Switches, SwModels


class SwitchesForm(forms.ModelForm):
    class Meta:
        model = Switches
        fields = ['name', 'ip_switch']
    name = forms.ModelChoiceField(
        queryset=SwModels.objects.all(), label="Модель", empty_label=None)
    ip_switch = forms.CharField(max_length=39, help_text="ip address")
