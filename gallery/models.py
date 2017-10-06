from django.db import models
from django.core.urlresolvers import reverse
from main.models import CommonMain


class Gallery(CommonMain):
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение",
                              help_text="Выберите изображение новости")
    min_image = models.ImageField(null=True, blank=True, verbose_name="Миниатюра",
                                  help_text="Выберите миниатюру")
    name = models.CharField(max_length=250, verbose_name="Название изображения", default="Изображения")
    brief = models.CharField(max_length=500, verbose_name="Краткое описание",
                             null=True, blank=True, help_text="Не более 500 знаков")

    class Meta:
        verbose_name_plural = "Галерея"

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'slug': self.slug})
