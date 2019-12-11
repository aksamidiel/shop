from django.shortcuts import render
from django.views.generic.list import ListView
from escooters.models import EScooter
from django.db.models import Q
from escooters.views import escooter_quantity_in_cart


class LatestView(ListView):
    model = EScooter
    template_name = 'homepage/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        escooter_quantity_in_cart(self, context)
        return context

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.order_by('-updated_date')[0:4]
