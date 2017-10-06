from django.contrib import admin
from .models import AboutUs, AboutCustomer, Team, Customers


# # Register your models here.
class TeamAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    date_hierarchy = 'date'
    list_display = ('name', 'job_title', 'slug', 'phone', 'image', 'number')
    list_filter = ('name', 'job_title',)
    list_editable = ('number',)
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Team, TeamAdmin)


class CustomerAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    date_hierarchy = 'date'
    list_display = ('name', 'slug', 'phone', 'image', 'number')
    list_filter = ('name', )
    list_editable = ('number',)
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Customers, CustomerAdmin)


@admin.register(AboutUs, AboutCustomer)
class AboutUsAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_display = ('name', 'slug', 'image', 'number')
    list_editable = ('number',)
    list_filter = ('name',)
    filter_horizontal = ('customers', 'team')
    prepopulated_fields = {"slug": ("title",)}


