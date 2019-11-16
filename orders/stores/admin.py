from django.contrib import admin
from .models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Contact

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


class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('model', 'external_id', 'product', 'shop', 'quantity', 'price', 'price_rrc', )
    search_fields = ('model', 'external_id', 'product', 'shop', )


admin.site.register(ProductInfo, ProductInfoAdmin)


class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


admin.site.register(Parameter, ParameterAdmin)


class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ('product_info', 'parameter', 'value')
    search_fields = ('product_info', 'parameter', )


admin.site.register(ProductParameter, ProductParameterAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'phone',)
    search_fields = ('user', 'city', 'street', 'phone', )


admin.site.register(Contact, ContactAdmin)
