from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from comments.forms import CommentCreateForm
from shopcart.models import Cart
from .models import EScooter
from .forms import EScooterForm
from django.db.models import Q


# Create your views here.
def escooter_quantity_in_cart(self, context):     # количество заказов в корзине
    cart_id = self.request.session.get('cart_id', '0')
    if cart_id != '0':
        context['quantity'] = Cart.objects.get(pk=cart_id).escooters_in_cart_count
    else:
        context['quantity'] = cart_id
    return context


class EScooterList(ListView):
    model = EScooter
    template_name = 'escooters/escooter_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/escooters/all'
        escooter_quantity_in_cart(self, context)
        return context

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        search = self.request.GET.get('search_escooter', 0)
        if qs.filter(Q(name__icontains=search) | Q(manufacturer__icontains=search)).distinct().exists():
            return qs.filter(Q(name__icontains=search) | Q(manufacturer__icontains__icontains=search)).distinct()
        return qs.order_by('name')


class EScooterDetail(DetailView):
    model = EScooter
    template_name = 'escooters/escooter_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logout_redirect'] = '/escooters/escooter/{}'.format(self.object.pk)
        checkout_form = CommentCreateForm()
        checkout_form.fields['commented_order'].initial = self.object
        checkout_form.fields['commented_user'].initial = self.request.user
        context['form'] = checkout_form
        escooter_quantity_in_cart(self, context)
        return context


class EScooterCreate(CreateView, PermissionRequiredMixin):
    model = EScooter
    template_name = 'escooters/create_form.html'
    form_class = EScooterForm
    permission_required = 'escooters.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('escooter-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('escooter-list-view')
        return reverse_lazy('escooter-create-view')


class EScooterUpdate(UpdateView, PermissionRequiredMixin):
    model = EScooter
    template_name = 'escooters/update_form.html'
    form_class = EScooterForm
    permission_required = 'escooters.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('escooter-detail-view', kwargs={'pk': self.object.pk})
        return reverse_lazy('escooter-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class EScooterDelete(DeleteView, PermissionRequiredMixin):
    model = EScooter
    template_name = 'escooters/delete_form.html'
    permission_required = 'escooters.edit_content'

    def get_success_url(self):
        return reverse_lazy('escooter-list-view')
