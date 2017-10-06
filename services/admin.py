from django.contrib import admin
from services.models import Service


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    date_hierarchy = 'date'
    list_display = ('name', 'slug', 'min_image', 'number')
    list_filter = ('name',)
    list_editable = ('number',)
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Service, ServiceAdmin)