from django import forms
from django.forms import ModelForm
from shopcart.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'fname', 'lname', 'email', 'pass']


class UpdateUserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email']


class UserCreateLoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields
