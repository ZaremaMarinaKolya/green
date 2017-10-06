from django.db import models
from django.core.urlresolvers import reverse
from main.models import CommonMain


class News(CommonMain):
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение",
                              help_text="Выберите изображение новости")
    min_image = models.ImageField(null=True, blank=True, verbose_name="Миниатюра",
                                  help_text="Выберите миниатюру новости")
    name = models.CharField(max_length=250, verbose_name="Название новости", default="Новость")
    brief = models.CharField(max_length=500, verbose_name="Краткое описание",
                             null=True, blank=True, help_text="Не более 500 знаков")

    class Meta:
        verbose_name_plural = "Новости"

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'slug': self.slug})


class Opinion(CommonMain):
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение",
                              help_text="Выберите изображение отзыва")
    min_image = models.ImageField(null=True, blank=True, verbose_name="Миниатюра",
                                  help_text="Выберите миниатюру отзыва")
    name = models.CharField(max_length=250, verbose_name="Название отзыва", default="Отзыв")
    brief = models.CharField(max_length=500, verbose_name="Краткое описание",
                             null=True, blank=True, help_text="Не более 500 знаков")

    class Meta:
        verbose_name_plural = "Отзывы"

    def get_absolute_url(self):
        return reverse('opinion-detail', kwargs={'slug': self.slug})
