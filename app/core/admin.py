"""
Django admin configuration for core app
"""

from django.contrib import admin
from django.utils.translation import gettext as translate_text
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    """
    Define the user model for admin
    """
    ordering = ['id']
    list_display = ['email', 'name']
    readonly_fields = ['last_login']
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password'
                )
            }
        ),
        (
            translate_text('Personal Info'),
            {
                'fields': (
                    'name',
                )
            }
        ),
        (
            translate_text('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (
            translate_text('Important dates'),
            {
                'fields': (
                    'last_login',
                )
            }
        )
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_staff',
                    'is_active',
                    'is_superuser',
                )
            }
        ),
    )


admin.site.register(models.User, UserAdmin)
