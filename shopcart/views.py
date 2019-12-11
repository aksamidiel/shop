from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from django.views.generic.list import ListView
from shopcart.models import EScooterInCart, Cart
from escooters.models import EScooter
from .forms import AddEScooterForm
from reference.models import OrderStatus
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from escooters.views import escooter_quantity_in_cart

new_order_status = OrderStatus.objects.get(pk=1)


# Create your views here.

class AddEscooterToCart(UpdateView):
    model = EScooterInCart
    form_class = AddEScooterForm
    template_name = 'cart/add-escooter.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        if self.request.user.is_anonymous:
            user = None
        else:
            user = self.request.user
        cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user})
        self.request.session['cart_id'] = cart.pk
        escooter_pk = self.kwargs.get('pk')
        escooter = EScooter.objects.get(pk=escooter_pk)
        escooter_in_cart, created = self.model.objects.get_or_create(cart=cart, escooter=escooter,
                                                                     defaults={'quantity': 1})
        if not created:
            escooter_in_cart.quantity += 1
        return escooter_in_cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '/')
        escooter_quantity_in_cart(self, context)
        return context

    def get_success_url(self):
        if self.request.POST.get('back'):
            product = self.model.objects.get(pk=self.object.pk)
            if product.quantity > 1:
                product.quantity -= 1
                product.save()
            else:
                product.delete()
        return self.request.POST.get('next', '/')


class CartView(DetailView):
    model = Cart
    template_name = 'cart/view-cart.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        if self.request.user.is_anonymous:
            user = None
        else:
            user = self.request.user
        cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user})
        return cart

    # def get_context_data(self, **kwargs):
    # context = super().get_context_data(**kwargs)
    # checkout_form = CheckOutOrderForm()
    # checkout_form.fields['cart'].initial = self.object
    # checkout_form.fields['status'].initial = new_order_status
    # context['form'] = checkout_form
    # book_quantity_in_cart(self, context)
    # return context


class DeleteBookFromCart(DeleteView):
    model = EScooterInCart
    template_name = 'cart/delete-escooter.html'

    def get_success_url(self):
        return reverse_lazy('view-cart')


class CartUserList(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'cart/cart_user_list.html'
    login_url = '/auth/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        escooter_quantity_in_cart(self, context)
        return context

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        current_user = self.request.user
        return qs.filter(user=current_user)
