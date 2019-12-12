from abc import ABC

from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from cart.models import User
from django.urls import reverse_lazy
from .forms import CreateUserLoginForm, UpdateUserLoginForm, UserCreationForm


# Create your views here.

class LoginViewPage(auth_views.LoginView):
    template_name = 'loginsys/login.html'


class LogoutViewPage(auth_views.LogoutView):
    extra_context = 'None'


class PasswordResetViewPage(auth_views.PasswordResetView):
    template_name = 'loginsys/password_templates/password_reset_form.html'
    email_template_name = 'loginsys/password_templates/password_reset_email.html'
    subject_template_name = 'loginsys/password_templates/password_reset_subject.txt'
    success_url = '/'


class PasswordResetConfirmViewPage(auth_views.PasswordResetConfirmView):
    template_name = 'loginsys/password_templates/password_reset_confirm.html'
    success_url = '/'


class CreateUser(CreateView):
    model = User
    template_name = 'loginsys/registration/create_user.html'
    form_class = CreateUserLoginForm
    form_class = UserCreationForm
    success_url = reverse_lazy('log-in')


class UpdateUser(UpdateView):
    model = User
    template_name = "loginsys/registration/update_user.html"
    form_class = UpdateUserLoginForm

    def get_success_url(self):
        print(self.object)
        return reverse_lazy('view-user', kwargs={'pk': self.object.pk})


class ViewUser(DetailView):
    model = User
    template_name = "loginsys/registration/view_user.html"


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'loginsys/registration/password_change_form.html'
    success_url = reverse_lazy('change-password-done')


class PasswordChangeDone(auth_views.PasswordChangeDoneView):
    template_name = 'loginsys/registration/password_change_done.html'
