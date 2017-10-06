from django.db import models


# Abstract model
class CommonSlider(models.Model):
    image = models.ImageField(null=True, blank=False, verbose_name="Изображение",
                              help_text="Выберите изображения для слайдера (3-5 изображений)")
    name = models.CharField(max_length=250, verbose_name="Название", default="Слайд")
    text = models.CharField(max_length=250, verbose_name="Содержание", null=True, blank=True)
    url = models.URLField(max_length=500, verbose_name="URL-адрес", null=True, blank=True)
    number = models.IntegerField(verbose_name="Порядок",
                                 null=True, blank=True, help_text="Установленное число "
                                                                  "будет влиять на очерёдность "
                                                                  "отображения блока")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Slider1(CommonSlider):
    class Meta:
        verbose_name_plural = "Слайдер 1"


class Slider2(CommonSlider):
    class Meta:
        verbose_name_plural = "Слайдер 2"


class Slider3(CommonSlider):
    class Meta:
        verbose_name_plural = "Слайдер 3"


class Slider4(CommonSlider):
    class Meta:
        verbose_name_plural = "Слайдер 4"


class Slider5(CommonSlider):
    class Meta:
        verbose_name_plural = "Слайдер 5"

