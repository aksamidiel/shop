from django import forms
from django.forms import ModelForm
from cart.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class UpdateUserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserCreateLoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields
