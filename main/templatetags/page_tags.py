from django import template
from green.settings import MEDIA_URL
from slider.models import Slider1, Slider2, Slider3, Slider4, Slider5
from services.models import Service
from news.models import News, Opinion
from gallery.models import Gallery
from banner.models import BannerOne, BannerTwo, BannerThree
from spoiler.models import Spoiler1, Spoiler2, Spoiler3
from html_parts.models import HtmlOne, HtmlTwo, HtmlThree, HtmlFour, HtmlFive, HtmlSix, HtmlSeven, HtmlEight, \
    HtmlNine, HtmlTen
from main.models import PageCategory, Page


register = template.Library()


# Sliders
@register.inclusion_tag('tags/sliders/slider1.html', takes_context=True)
def slider1(context):
    slide = Slider1.objects.all().order_by('number')
    return {'sliders': slide, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/sliders/slider2.html', takes_context=True)
def slider2(context):
    slide = Slider2.objects.all().order_by('number')
    return {'sliders': slide, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/sliders/slider3.html', takes_context=True)
def slider3(context):
    slide = Slider3.objects.all().order_by('number')
    return {'sliders': slide, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/sliders/slider4.html', takes_context=True)
def slider4(context):
    slide = Slider4.objects.all().order_by('number')
    return {'sliders': slide, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/sliders/slider5.html', takes_context=True)
def slider5(context):
    slide = Slider5.objects.all().order_by('number')
    return {'sliders': slide, 'MEDIA': MEDIA_URL}


# services
@register.inclusion_tag('tags/services/services-panel.html', takes_context=True)
def services_panel(context):
    services = Service.objects.order_by('number')
    return {'services': services, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/services/service-tabs.html', takes_context=True)
def service_tabs(context):
    services = Service.objects.order_by('number')
    return {'services': services, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/services/service-list.html', takes_context=True)
def service_list(context):
    services = Service.objects.order_by('number')
    return {'services': services, 'MEDIA': MEDIA_URL}


# news
@register.inclusion_tag('tags/news/news-panel.html', takes_context=True)
def news_panel(context):
    news = News.objects.order_by('number')
    return {'news': news, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/news/opinions-panel.html', takes_context=True)
def opinion_panel(context):
    opinions = Opinion.objects.order_by('number')
    return {'opinions': opinions, 'MEDIA': MEDIA_URL}


# gallery
@register.inclusion_tag('tags/gallery/gallery-showcase-one.html', takes_context=True)
def gallery_showcase_one(context):
    showcase = Gallery.objects.order_by('number')
    return {'showcase': showcase, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/gallery/gallery-showcase-two.html', takes_context=True)
def gallery_showcase_two(context):
    showcase = Gallery.objects.order_by('number')
    return {'showcase': showcase, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/gallery/gallery-showcase-three.html', takes_context=True)
def gallery_showcase_three(context):
    showcase = Gallery.objects.order_by('number')
    return {'showcase': showcase, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/gallery/gallery-showcase-five.html', takes_context=True)
def gallery_showcase_five(context):
    showcase = Gallery.objects.order_by('number')
    return {'showcase': showcase, 'MEDIA': MEDIA_URL}


# Banners
@register.inclusion_tag('tags/banner/banner-1.html', takes_context=True)
def banner_one(context):
    banner = BannerOne.objects.order_by('number')
    return {'banner': banner, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/banner/banner-2.html', takes_context=True)
def banner_two(context):
    banner = BannerTwo.objects.order_by('number')
    return {'banner': banner, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/banner/banner-3.html', takes_context=True)
def banner_three(context):
    banner = BannerThree.objects.order_by('number')
    return {'banner': banner, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/spoiler/spoiler1.html', takes_context=True)
def spoiler_one(context):
    spoiler = Spoiler1.objects.order_by('number')
    return {'spoiler': spoiler, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/spoiler/spoiler2.html', takes_context=True)
def spoiler_two(context):
    spoiler = Spoiler2.objects.order_by('number')
    return {'spoiler': spoiler, 'MEDIA': MEDIA_URL}


@register.inclusion_tag('tags/spoiler/spoiler3.html', takes_context=True)
def spoiler_three(context):
    spoiler = Spoiler3.objects.order_by('number')
    return {'spoiler': spoiler, 'MEDIA': MEDIA_URL}


# Html inserts
@register.inclusion_tag('tags/htmls/html1.html', takes_context=True)
def html_one(context):
    html = HtmlOne.objects.order_by('number')
    return {'html_parts': html}


@register.inclusion_tag('tags/htmls/html2.html', takes_context=True)
def html_two(context):
    html = HtmlTwo.objects.order_by('number')
    return {'html_parts': html}


@register.inclusion_tag('tags/htmls/html3.html', takes_context=True)
def html_three(context):
    html = HtmlThree.objects.order_by('number')
    return {'html_parts': html}


@register.inclusion_tag('tags/htmls/html4.html', takes_context=True)
def html_four(context):
    html = HtmlFour.objects.order_by('number')
    return {'html_parts': html}


@register.inclusion_tag('tags/htmls/html5.html', takes_context=True)
def html_five(context):
    html = HtmlFive.objects.order_by('number')
    return {'html_parts': html}


@register.inclusion_tag('tags/htmls/html6.html', takes_context=True)
def html_six(context):
    html = HtmlSix.objects.order_by('number')
    return {'html_parts': html}


@register.inclusion_tag('tags/htmls/html7.html', takes_context=True)
def html_seven(context):
    html = HtmlSeven.objects.order_by('number')
    return {'html_parts': html}


@register.inclusion_tag('tags/htmls/html8.html', takes_context=True)
def html_eight(context):
    html = HtmlEight.objects.order_by('number')
    return {'html_parts': html}


@register.inclusion_tag('tags/htmls/html9.html', takes_context=True)
def html_nine(context):
    html = HtmlNine.objects.order_by('number')
    return {'html_parts': html}


@register.inclusion_tag('tags/htmls/html10.html', takes_context=True)
def html_ten(context):
    html = HtmlTen.objects.order_by('number')
    return {'html_parts': html}


# menu
@register.inclusion_tag('tags/menu/cat-menu.html', takes_context=True)
def cat_menu(context):
    menu = list()
    categories = PageCategory.objects.filter(menu=True).order_by('number')
    for one in categories:
        page = dict()
        page['name'] = one.name
        page['list_one']= Page.objects.filter(category__slug=one.slug, type_page = 'style-one').order_by('number')
        page['list_two'] = Page.objects.filter(category__slug=one.slug, type_page='style-two').order_by('number')
        page['list_three'] = Page.objects.filter(category__slug=one.slug, type_page='style-three').order_by('number')
        page['list_four'] = Page.objects.filter(category__slug=one.slug, type_page='style-four').order_by('number')
        page['list_five'] = Page.objects.filter(category__slug=one.slug, type_page='style-five').order_by('number')
        menu.append(page)
    return {'menu': menu}
