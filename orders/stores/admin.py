from django.contrib import admin
from .models import Shop, Category

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
