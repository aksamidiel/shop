from django.contrib import admin
from .models import Cart, EScooterInCart


# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'escooters_in_cart_count', 'pk']

    class Meta:
        model = Cart


admin.site.register(Cart, CartAdmin)
admin.site.register(EScooterInCart)
