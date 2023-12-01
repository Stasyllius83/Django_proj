from django.contrib import admin

from catalog.models import Category, Product


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
