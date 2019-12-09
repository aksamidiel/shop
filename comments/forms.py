from django import forms
from django.forms import ModelForm
from .models import *


class CommentCreateForm(ModelForm):
    class Meta:
        model = CommentProduct
        fields = ['commented_order', 'commented_to_order', 'commented_user']
        widgets = {'commented_order': forms.HiddenInput, 'commented_user': forms.HiddenInput}  # скрывает поля
