from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'school', 'email', 'enrollment_date')
    search_fields = ('first_name', 'last_name', 'email', 'school__name')
    list_filter = ('school', 'gender', 'enrollment_date')
