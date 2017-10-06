from django.contrib import admin
from banner.models import BannerOne, BannerTwo, BannerThree, BannerPage
# Register your models here.


@admin.register(BannerOne, BannerTwo, BannerThree, BannerPage)
class BannerOneAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    date_hierarchy = 'date'
    list_display = ('name', 'brief', 'slug', 'image', 'number')
    list_filter = ('name',)
    list_editable = ('number',)
    prepopulated_fields = {"slug": ("title",)}



