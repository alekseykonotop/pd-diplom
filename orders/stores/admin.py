from django.contrib import admin
from .models import Shop, Category, Product

# Register your models here.


class ShopAdmin(admin.ModelAdmin):
    list_display = ('trademark_name', 'slug', 'state', )
    search_fields = ('trademark_name', 'state', )
    prepopulated_fields = {'slug': ('trademark_name',)}


admin.site.register(Shop, ShopAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', )
    search_fields = ('name', 'category', )


admin.site.register(Product, ProductAdmin)