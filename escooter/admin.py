from django.contrib import admin
from .models import *


# Register your models here.
class EScooterAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'updated_date']  # отображаются указанные поля
    list_filter = ("name", 'author', 'serie', 'manufacturer')  # отфильтровать по полям

    # search_fields = [field.name for field in ._meta.fields]  # поиск по всем полям

    class Meta:
        model = EScooter


admin.site.register(EScooter, EScooterAdmin)
