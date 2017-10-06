from django.db import models
from django.core.urlresolvers import reverse
from main.models import CommonMain


# Create your models here.
class Service(CommonMain):
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение",
                              help_text="Выберите изображения услуги")
    min_image = models.ImageField(null=True, blank=True, verbose_name="Миниатюра",
                                  help_text="Выберите миниатюру услуги")
    brief = models.CharField(max_length=500, verbose_name="Краткое описание",
                             null=True, blank=True, help_text="Не более 500 знаков")
    phone = models.CharField(max_length=50, verbose_name="Телефон",
                             help_text="Не более 50 знаков", null=True, blank=True)
    messenger = models.CharField(max_length=100, verbose_name="Messenger",
                                 help_text="Не более 100 знаков", null=True, blank=True)
    social_one = models.URLField(max_length=500, verbose_name="URL-адрес 1",
                                 help_text="Вставьте URL-адрес социальной сети услуги", null=True, blank=True)
    social_two = models.URLField(max_length=500, verbose_name="URL-адрес 2",
                                 help_text="Вставьте URL-адрес социальной сети услуги", null=True, blank=True)
    social_three = models.URLField(max_length=500, verbose_name="URL-адрес 3",
                                   help_text="Вставьте URL-адрес социальной сети услуги", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Услуги"

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'slug': self.slug})
