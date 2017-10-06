from django.db import models
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField


# Abstract model
class Banner(models.Model):
    title = models.CharField(max_length=250, null=True, help_text="Введите заголовок страницы",)
    descriptions = models.TextField(max_length=1000, help_text="Введите описание для поисковых систем",
                                    null=True, blank=True)
    keywords = models.TextField(max_length=1000, help_text="Введите ключевые слова для поисковых систем",
                                    null=True, blank=True)
    slug = models.SlugField(null=True, unique=True, help_text="Slug влияет на формирование url адреса"
                                                              " и должен быть уникальным")
    name = models.CharField(max_length=250, verbose_name="Название страницы", default="Страница")
    content = RichTextUploadingField(verbose_name="Содержание страницы", null=True, blank=True)
    date = models.DateField(auto_now=False, auto_created=False, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение",
                              help_text="Выберите изображение баннера")
    name = models.CharField(max_length=250, verbose_name="Заголовок баннера", default="Баннер")
    brief = models.CharField(max_length=500, verbose_name="Краткий лозунг",
                             null=True, blank=True, help_text="Не более 500 знаков")
    url = models.URLField(max_length=500, verbose_name="URL-адрес баннера",
                          help_text="Вставьте URL-адрес", null=True, blank=True)
    number = models.IntegerField(verbose_name="Порядок",
                                 null=True, blank=True, help_text="Установленное число "
                                                                  "будет влиять на очерёдность "
                                                                  "отображения блока")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('banner-one-detail', kwargs={'slug': self.slug})


class BannerOne(Banner):

    class Meta:
        verbose_name_plural = "Баннер 1"

    def get_absolute_url(self):
        return reverse('banner-one-detail', kwargs={'slug': self.slug})


class BannerTwo(Banner):

    class Meta:
        verbose_name_plural = "Баннер 2"

    def get_absolute_url(self):
        return reverse('banner-two-detail', kwargs={'slug': self.slug})


class BannerThree(Banner):

    class Meta:
        verbose_name_plural = "Баннер 3"

    def get_absolute_url(self):
        return reverse('banner-three-detail', kwargs={'slug': self.slug})


class BannerPage(Banner):

    class Meta:
        verbose_name_plural = "Баннер, связанный со страницей"

    def get_absolute_url(self):
        return reverse('banner-page-detail', kwargs={'slug': self.slug})

