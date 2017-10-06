from django.db import models
from django.core.urlresolvers import reverse
from main.models import CommonMain


# Create your models here.
class Team(CommonMain):
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение",
                              help_text="Выберите изображения сотрудника")
    name = models.CharField(max_length=250, verbose_name="Имя сотрудника", default="Сотрудник")
    job_title = models.CharField(max_length=250, verbose_name="Должность сотрудника", default="Сотрудник")
    brief = models.CharField(max_length=500, verbose_name="Краткое описание",
                             null=True, blank=True, help_text="Не более 500 знаков")
    phone = models.CharField(max_length=50, verbose_name="Телефон",
                             help_text="Не более 50 знаков", null=True, blank=True)
    messenger = models.CharField(max_length=100, verbose_name="Messenger",
                                 help_text="Не более 100 знаков", null=True, blank=True)
    social_one = models.URLField(max_length=500, verbose_name="URL-адрес 1",
                                 help_text="Вставьте URL-адрес социальной сети сотрудника", null=True, blank=True)
    social_two = models.URLField(max_length=500, verbose_name="URL-адрес 2",
                                 help_text="Вставьте URL-адрес социальной сети сотрудника", null=True, blank=True)
    social_three = models.URLField(max_length=500, verbose_name="URL-адрес 3",
                                   help_text="Вставьте URL-адрес социальной сети сотрудника", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Сотрудники"

    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={'slug': self.slug})


class Customers(CommonMain):
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение",
                              help_text="Выберите логотип клиента")
    name = models.CharField(max_length=250, verbose_name="Название фирмы", default="Фирма")
    brief = models.CharField(max_length=500, verbose_name="Краткое описание",
                             null=True, blank=True, help_text="Не более 500 знаков")
    phone = models.CharField(max_length=50, verbose_name="Телефон",
                             help_text="Не более 50 знаков", null=True, blank=True)
    messenger = models.CharField(max_length=100, verbose_name="Messenger",
                                 help_text="Не более 100 знаков", null=True, blank=True)
    social_one = models.URLField(max_length=500, verbose_name="URL-адрес 1",
                                 help_text="Вставьте URL-адрес социальной сети клиента", null=True, blank=True)
    social_two = models.URLField(max_length=500, verbose_name="URL-адрес 2",
                                 help_text="Вставьте URL-адрес социальной сети клиента", null=True, blank=True)
    social_three = models.URLField(max_length=500, verbose_name="URL-адрес 3",
                                   help_text="Вставьте URL-адрес социальной сети клиента", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Клиенты"

    def get_absolute_url(self):
        return reverse('customer-detail', kwargs={'slug': self.slug})


class AboutUs(CommonMain):
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение",
                              help_text="Выберите изображение")
    team = models.ManyToManyField(Team, verbose_name="Сотрудники",)
    customers = models.ManyToManyField(Customers, verbose_name="Клиенты",)

    class Meta:
        verbose_name_plural = "Страница о нас"

    def get_absolute_url(self):
        return reverse('about', kwargs={'slug': self.slug})


class AboutCustomer(CommonMain):
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение",
                              help_text="Выберите изображение")
    team = models.ManyToManyField(Team, verbose_name="Сотрудники",)
    customers = models.ManyToManyField(Customers, verbose_name="Клиенты",)

    class Meta:
        verbose_name_plural = "Страница о клиентах"

    def get_absolute_url(self):
        return reverse('about-customer', kwargs={'slug': self.slug})

