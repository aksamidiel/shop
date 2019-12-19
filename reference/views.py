from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .forms import *
from .models import *
from escooters.views import escooter_quantity_in_cart


# Create your views here.

def get_cancel_url(self, context):
    context['cancel_url'] = self.get_success_url()
    return context


class ReferenceView(TemplateView):
    template_name = 'reference/references.html'  # шаблон странички с ссылками

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/refs/all'
        escooter_quantity_in_cart(self, context)
        return context


class ManufacturerDetail(TemplateView):
    model = Manufacturer
    template_name = 'reference/detail/manufacturer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'manufacturer-update-view'
        context['delete_url'] = 'manufacturer-delete-view'
        manufacturer_pk = self.kwargs.get('pk')
        context['logout_redirect'] = '/refs/manufacturer/{}'.format(manufacturer_pk)
        escooter_quantity_in_cart(self, context)
        return context


class SerieDetail(DetailView):
    model = Series
    template_name = 'reference/detail/series_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_url'] = 'serie-update-view'
        context['delete_url'] = 'serie-delete-view'
        serie_pk = self.kwargs.get('pk')
        context['logout_redirect'] = '/refs/serie/{}'.format(serie_pk)
        escooter_quantity_in_cart(self, context)
        return context


class ManufacturerList(ListView):
    model = Manufacturer
    template_name = 'reference/list/manufacturer_list.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        search = self.request.GET.get('name', 0)
        if qs.filter(name__icontains=search).exists():
            return qs.filter(name__icontains=search)
        else:
            return qs.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/refs/author'
        escooter_quantity_in_cart(self, context)
        return context


class SerieList(ListView):
    model = Series
    template_name = 'reference/list/series_list.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        search = self.request.GET.get('name', 0)
        if qs.filter(name__icontains=search).exists():
            return qs.filter(name__icontains=search)
        else:
            return qs.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/refs/serie'
        escooter_quantity_in_cart(self, context)
        return context


class ManufacturerCreate(PermissionRequiredMixin, CreateView):
    model = Manufacturer
    template_name = 'reference/form/create_form.html'
    form_class = ManufacturerForm

    permission_required = 'escooters.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('manufacturer-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('manufacturer-list-view')
        return reverse_lazy('manufacturer-create-view')


class SerieCreate(PermissionRequiredMixin, CreateView):
    model = Series
    template_name = 'reference/form/create_form.html'
    form_class = SerieForm

    permission_required = 'escooters.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('serie-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('serie-list-view')
        return reverse_lazy('serie-create-view')


class ManufacturerUpdate(PermissionRequiredMixin, UpdateView):
    model = Manufacturer
    template_name = 'reference/form/update_form.html'
    form_class = ManufacturerForm
    permission_required = 'escooters.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('manufacturer-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('manufacturer-list-view')


class SerieUpdate(PermissionRequiredMixin, UpdateView):
    model = Series
    template_name = 'reference/form/update_form.html'
    form_class = SerieForm
    permission_required = 'escooters.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('serie-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('serie-list-view')


class ManufacturerDelete(PermissionRequiredMixin, DeleteView):
    model = Manufacturer
    template_name = 'reference/form/delete_form.html'
    permission_required = 'manufacturer.edit_content'

    def get_success_url(self):
        return reverse_lazy('manufacturer-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)


class SerieDelete(PermissionRequiredMixin, DeleteView):
    model = Series
    template_name = 'reference/form/delete_form.html'
    permission_required = 'manufacturer.edit_content'

    def get_success_url(self):
        return reverse_lazy('serie-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_cancel_url(self, context)
