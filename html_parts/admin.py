from django.contrib import admin
from html_parts.models import HtmlOne, HtmlTwo, HtmlThree, HtmlFour, HtmlFive, HtmlSix, HtmlSeven, HtmlEight, HtmlNine, HtmlTen


@admin.register(HtmlOne, HtmlTwo, HtmlThree, HtmlFour, HtmlFive, HtmlSix, HtmlSeven, HtmlEight, HtmlNine, HtmlTen)
class HtmlOneAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    empty_value_display = '-пусто-'
    list_display = ('name', 'html', 'date', 'number')
    list_filter = ('date', 'name')
    list_editable = ('number',)
