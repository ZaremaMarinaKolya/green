from django.contrib import admin
from news.models import News, Opinion
# Register your models here.


@admin.register(News, Opinion)
class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    empty_value_display = '-пусто-'
    list_display = ('name', 'date', 'min_image', 'brief', 'number')
    list_editable = ('number',)
    list_filter = ('date',)
    prepopulated_fields = {"slug": ("title",)}

