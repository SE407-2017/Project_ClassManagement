from django.contrib import admin
from .models import Category, Course

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',  'stock',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Course, CourseAdmin)
