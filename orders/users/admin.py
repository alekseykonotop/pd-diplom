from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'last_name', 'first_name', 'middle_name',
                    'company', 'position', 'type', 'is_active', )
    list_filter = ('email', 'last_name', 'is_active', )
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Дополнительные сведения', {
            'fields': ('last_name', 'first_name', 'middle_name', ),
            'description': 'Персональная информация'
        }),
        ('Тип пользователя', {
            'fields': ('type', ),
            'description': 'Тип пользователя'
        }),
        ('Информация о компании', {
            'fields': ('company', 'position', ),
            'description': 'Наименование компании и должность'
        }),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'last_name', 'first_name', 'middle_name',
                       'company', 'position', 'type', 'is_active')}),
    )
    search_fields = ('email', 'last_name', )
    ordering = ('email', 'last_name', )


admin.site.register(User, CustomUserAdmin)

