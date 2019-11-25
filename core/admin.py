from django.contrib import admin
from .models import Category, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name', 'description')}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_date_at', 'updated_date_at', 'description']
    list_filter = ['available', 'created_date_at', 'updated_date_at']
    list_editable = ['price', 'stock', 'available', 'description']
    prepopulated_fields = {'slug': ('name', 'description')}


admin.site.register(Product, ProductAdmin)
