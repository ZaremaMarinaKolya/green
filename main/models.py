from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import date as d
from django.core.urlresolvers import reverse
from spoiler.models import SpoilerPage
from banner.models import BannerPage


# Abstract model
class CommonMain(models.Model):
    title = models.CharField(max_length=250, null=True, help_text="Введите заголовок страницы",)
    descriptions = models.TextField(max_length=1000, help_text="Введите описание для поисковых систем",
                                    null=True, blank=True)
    keywords = models.TextField(max_length=1000, help_text="Введите ключевые слова для поисковых систем",
                                    null=True, blank=True)
    slug = models.SlugField(null=True, unique=True, help_text="Slug влияет на формирование url адреса"
                                                              " и должен быть уникальным")
    name = models.CharField(max_length=250, verbose_name="Название страницы", default="Страница")
    content = RichTextUploadingField(verbose_name="Содержание страницы", null=True, blank=True)
    date = models.DateField(verbose_name="Дата", default=d.today(), blank=True, null=True)
    number = models.IntegerField(verbose_name="Порядок",
                                 null=True, blank=True, help_text="Установленное число "
                                                                  "будет влиять на очерёдность "
                                                                  "отображения блока")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# Create your models here.
class Home(CommonMain):
    slug = models.SlugField(null=True, unique=True, editable=False)
    date = models.DateField(auto_now=False, auto_created=False, blank=True, null=True, editable=False)
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение",
                              help_text="Выберите изображение")
    number = models.IntegerField(verbose_name="Порядок",
                                 null=True, blank=True, editable=False)

    class Meta:
        verbose_name_plural = "Главная"

    def delete(self):
        if self.slug == 'index':
            raise ValueError("Нельзя удалять основные страницы")
        super(Home, self).delete()

    def save(self):
        if self.slug != 'index':
            raise ValueError("Нельзя добавлять вторую главную страницу")
        super(Home, self).save()


class Contact(CommonMain):
    slug = models.SlugField(null=True, unique=True)
    date = models.DateField(auto_now=False, auto_created=False, blank=True, null=True, editable=False)
    address = models.CharField(max_length=250, null=True, blank=True, help_text="Введите адрес контактов")
    phone = models.CharField(max_length=250, null=True, blank=True, help_text="Введите телефон контактов")
    email = models.CharField(max_length=250, null=True, blank=True, help_text="Введите email контактов")
    map = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=250, blank=True, null=True)
    opening_hours = models.CharField(max_length=250, null=True, blank=True,
                                     help_text="Введите часы работы в виде: Monday - Friday: 9:00 AM to 5:00 PM")
    social_one = models.URLField(max_length=500, verbose_name="URL-адрес 1",
                                 help_text="Вставьте URL-адрес социальной сети компании", null=True, blank=True)
    social_two = models.URLField(max_length=500, verbose_name="URL-адрес 2",
                                 help_text="Вставьте URL-адрес социальной сети компании", null=True, blank=True)
    social_three = models.URLField(max_length=500, verbose_name="URL-адрес 3",
                                   help_text="Вставьте URL-адрес социальной сети компании", null=True, blank=True)
    social_four = models.URLField(max_length=500, verbose_name="URL-адрес 4",
                                  help_text="Вставьте URL-адрес социальной сети компании", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Контакты"

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'slug': self.slug})


class PageCategory(CommonMain):
    name = models.CharField(max_length=250, verbose_name="Название категории", default="Категория")
    menu = models.BooleanField(default=True,
                               verbose_name="Меню", help_text="Отметьте, если "
                                                              "категория должна отображаться как меню")

    class Meta:
        verbose_name_plural = "Категории страниц"

    def get_absolute_url(self):
        return reverse('page-category', kwargs={'slug': self.slug})


class Page(CommonMain):
    STYLE_OF_PAGE = (
        ('style-one', 'Стиль 1'),
        ('style-two', 'Стиль 2'),
        ('style-three', 'Стиль с баннером'),
        ('style-four', 'Стиль со спойлером'),
        ('style-five', 'Стиль с баннером и спойлером')
    )
    type_page = models.CharField(max_length=20,
                                 choices=STYLE_OF_PAGE,
                                 default='style-one', verbose_name='Стиль страницы',
                                 help_text='Необходимо выбрать стиль того, как будет отражаться страница')
    category = models.ManyToManyField(PageCategory, verbose_name="Категория",
                                      help_text="Одна или несколько категорий, к которым будет принадлежать страница", blank=True, null=True)
    banner = models.ManyToManyField(BannerPage, verbose_name="Баннер",
                                    help_text="Задайте, если ваш стиль поддерживает баннеры", blank=True, null=True)
    spoiler = models.ManyToManyField(SpoilerPage, verbose_name="Спойлер",
                                     help_text="Задайте, если ваш стиль поддерживает спойлеры", blank=True, null=True )

    class Meta:
        verbose_name_plural = "Дополнительные страницы"

    def get_page_one_url(self):
        return reverse('page-style-one', kwargs={'type_page': self.type_page, 'slug': self.slug})

    def get_page_two_url(self):
        return reverse('page-style-two', kwargs={'type_page': self.type_page, 'slug': self.slug})

    def get_page_three_url(self):
        return reverse('page-style-three', kwargs={'type_page': self.type_page, 'slug': self.slug})

    def get_page_four_url(self):
        return reverse('page-style-four', kwargs={'type_page': self.type_page, 'slug': self.slug})

    def get_page_five_url(self):
        return reverse('page-style-five', kwargs={'type_page': self.type_page, 'slug': self.slug})




