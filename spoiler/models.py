from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
# Abstract model
class CommonSpoiler(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название", default="Spoiler")
    text = RichTextUploadingField(verbose_name="Содержание", null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    number = models.IntegerField(verbose_name="Порядок",
                                 null=True, blank=True, help_text="Установленное число "
                                                                  "будет влиять на очерёдность "
                                                                  "отображения блока")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Spoiler1(CommonSpoiler):
    class Meta:
        verbose_name_plural = "Spoiler 1"


class Spoiler2(CommonSpoiler):
    class Meta:
        verbose_name_plural = "Spoiler 2"


class Spoiler3(CommonSpoiler):
    class Meta:
        verbose_name_plural = "Spoiler 3"


class SpoilerPage(CommonSpoiler):
    class Meta:
        verbose_name_plural = "Spoiler for page"

