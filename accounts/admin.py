from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('School Access', {'fields': ('school', 'role')}),
    )
    list_display = UserAdmin.list_display + ('school', 'role')
    list_filter = UserAdmin.list_filter + ('role', 'school')
