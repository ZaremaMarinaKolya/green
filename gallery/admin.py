from django.contrib import admin
from gallery.models import Gallery

# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    date_hierarchy = 'date'
    list_display = ('name', 'slug', 'image', 'number')
    list_filter = ('name',)
    list_editable = ('number',)
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Gallery, GalleryAdmin)