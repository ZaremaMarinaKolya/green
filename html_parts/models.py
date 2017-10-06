from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class HtmlPart(models.Model):
    name = models.CharField(max_length=250, default="HTML", verbose_name="Название")
    html = RichTextUploadingField(help_text="Вставьте отредактированный текст или html")
    date = models.DateTimeField(auto_now=True)
    number = models.IntegerField(verbose_name="Порядок",
                                 null=True, blank=True, help_text="Установленное число "
                                                                  "будет влиять на очерёдность отображения блока")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class HtmlOne(HtmlPart):
    class Meta:
        verbose_name_plural = "HTML вставка 1"


class HtmlTwo(HtmlPart):
    class Meta:
        verbose_name_plural = "HTML вставка 2"


class HtmlThree(HtmlPart):
    class Meta:
        verbose_name_plural = "HTML вставка 3"


class HtmlFour(HtmlPart):
    class Meta:
        verbose_name_plural = "HTML вставка 4"


class HtmlFive(HtmlPart):
    class Meta:
        verbose_name_plural = "HTML вставка 5"


class HtmlSix(HtmlPart):
    class Meta:
        verbose_name_plural = "HTML вставка 6"


class HtmlSeven(HtmlPart):
    class Meta:
        verbose_name_plural = "HTML вставка 7"


class HtmlEight(HtmlPart):
    class Meta:
        verbose_name_plural = "HTML вставка 8"


class HtmlNine(HtmlPart):
    class Meta:
        verbose_name_plural = "HTML вставка 9"


class HtmlTen(HtmlPart):
    class Meta:
        verbose_name_plural = "HTML вставка 10"
