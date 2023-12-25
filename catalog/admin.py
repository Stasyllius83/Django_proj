from django.contrib import admin

from catalog.models import Category, Product, Version


# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'picture')
    list_filter = ('category',)
    search_fields = ('name', 'description',)
    list_display_links = ['name']


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'num_version', 'name_version', 'status_version')
    list_filter = ('product', 'status_version')
