from django.contrib import admin
from main.models import Home, Contact, PageCategory, Page


class HomeAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_display = ('name', 'slug', 'title', 'descriptions', 'image')
admin.site.register(Home, HomeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    date_hierarchy = 'date'
    list_display = ('name', 'slug', 'menu', 'date', 'number')
    list_editable = ('menu', 'number')
    list_filter = ('name', 'menu')
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(PageCategory, CategoryAdmin)


class PageAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    date_hierarchy = 'date'
    list_display = ('name', 'slug', 'type_page', 'number')
    list_editable = ('type_page', 'number')
    list_filter = ('name', 'type_page')
    filter_horizontal = ('banner', 'spoiler')
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Page, PageAdmin)


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    empty_value_display = '-пусто-'
    list_display = ('name', 'type', 'slug', 'date')
    list_filter = ('date',)
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Contact, ContactAdmin)
