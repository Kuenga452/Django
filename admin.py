from django.contrib import admin
from .models import Student  # Fixed spacing after 'from'

# Register your models here.
@admin.register(Student)  # Use decorator for cleaner registration
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'studentID', 'age')  # Show these fields in admin list view
