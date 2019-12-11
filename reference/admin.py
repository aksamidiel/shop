from django.contrib import admin
from .models import *


# Register your models here.
# админская панелька

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_filter = ['name']
    search_fields = ['name', 'country']
    ordering = ['country']

    class Meta:
        model = Manufacturer


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Series)
admin.site.register(OrderStatus)
