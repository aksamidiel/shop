from django import forms
from django.forms import ModelForm
from .models import *


class SearchForm(forms.Form):
    name = forms.CharField(label="Поиск по названию")


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country']


class SerieForm(ModelForm):
    class Meta:
        model = Series
        fields = ['name', 'description']

