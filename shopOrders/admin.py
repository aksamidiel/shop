from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.

class ShopOrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class ShopOrderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'first_name',
                    'last_name',
                    'email',
                    'address',
                    'postal_code',
                    'city',
                    'town',
                    'paid',
                    'updated']
    list_filter = ['paid',
                   'created',
                   'updated']
    inlines = [ShopOrderItemAdmin]

admin.site.register(Order, ShopOrderAdmin)
