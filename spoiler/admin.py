from django.contrib import admin
from spoiler.models import Spoiler1, Spoiler2, Spoiler3, SpoilerPage


# # Register your models here.
@admin.register(Spoiler1, Spoiler2, Spoiler3, SpoilerPage)
class SpoilerAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_display = ('name', 'date','number',)
    list_filter = ('name', )
    list_editable = ('number',)