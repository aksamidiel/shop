from django import forms
from django.forms import ModelForm
from .models import *


class AddEScooterForm(ModelForm):
    class Meta:
        model = EScooterInCart
        fields = ['cart', 'escooter', 'quantity']
        widgets = {'cart': forms.HiddenInput, 'escooter': forms.HiddenInput}
