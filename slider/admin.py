from django.contrib import admin
from slider.models import Slider1, Slider2, Slider3, Slider4, Slider5


# # Register your models here.
@admin.register(Slider1, Slider2, Slider3, Slider4, Slider5)
class PageAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_display = ('name', 'url', 'image', 'text', 'number',)
    list_filter = ('name', 'url',)
    list_editable = ('number',)


