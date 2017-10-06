from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from . import models as main
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from banner.models import BannerPage
from spoiler.models import SpoilerPage


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['page'] = main.Home.objects.get(slug = 'index')
        return context


def contact(request, slug):
    page = get_object_or_404(main.Contact, slug=slug)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        type = request.POST['type']
        if form.is_valid():
            cd = form.cleaned_data
            message = "Письмо для " + type + " от " + cd['email']+" " + cd["message"] + \
                      "\n Телефон: " + cd["phone"]
            send_mail(
                cd['name'],
                message,
                'lutynikoly@yandex.ru',
                ['lutynikoly@yandex.ru'],
            )
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'page': page })


def thanks(request):
    page = main.Contact.objects.get(slug = 'contact')
    return render(request, 'thanks.html', {'page': page,})


class PageCategory(TemplateView):
    context_object_name = 'page'
    template_name = 'page-category.html'

    def get_context_data(self, **kwargs):
        context = super(PageCategory, self).get_context_data(**kwargs)
        context['page'] = get_object_or_404(main.PageCategory, slug=kwargs['slug'])
        context['page_list_one'] = \
            main.Page.objects.filter(category__slug=kwargs['slug'], type_page ='style-one').order_by('number')
        context['page_list_two'] = \
            main.Page.objects.filter(category__slug=kwargs['slug'], type_page='style-two').order_by('number')
        context['page_list_three'] = \
            main.Page.objects.filter(category__slug=kwargs['slug'], type_page='style-three').order_by('number')
        context['page_list_four'] = \
            main.Page.objects.filter(category__slug=kwargs['slug'], type_page='style-four').order_by('number')
        context['page_list_five'] = \
            main.Page.objects.filter(category__slug=kwargs['slug'], type_page='style-five').order_by('number')
        return context


class PageStyleOne(TemplateView):
    context_object_name = 'page'
    template_name = 'page1.html'

    def get_context_data(self, **kwargs):
        context = super(PageStyleOne, self).get_context_data(**kwargs)
        context['page'] = get_object_or_404(main.Page, type_page=kwargs['type_page'], slug=kwargs['slug'])
        context['category'] = \
            main.PageCategory.objects.filter(page__slug=kwargs['slug']).order_by('number')
        return context


class PageStyleTwo(TemplateView):
    context_object_name = 'page'
    template_name = 'page2.html'

    def get_context_data(self, **kwargs):
        context = super(PageStyleTwo, self).get_context_data(**kwargs)
        context['page'] = get_object_or_404(main.Page, type_page=kwargs['type_page'], slug=kwargs['slug'])
        context['category'] = \
            main.PageCategory.objects.filter(page__slug=kwargs['slug']).order_by('number')
        context['category_pages_one'] = \
            set(main.Page.objects.filter(category__page__slug=kwargs['slug'], type_page ='style-one').order_by('number'))
        context['category_pages_two'] = \
            set(main.Page.objects.filter(category__page__slug=kwargs['slug'], type_page='style-two').order_by('number'))
        context['category_pages_three'] = \
            set(main.Page.objects.filter(category__page__slug=kwargs['slug'], type_page='style-three').order_by('number'))
        context['category_pages_four'] = \
            set(main.Page.objects.filter(category__page__slug=kwargs['slug'], type_page='style-four').order_by('number'))
        context['category_pages_five'] = \
            set(main.Page.objects.filter(category__page__slug=kwargs['slug'], type_page='style-five').order_by('number'))
        return context


class PageStyleThree(TemplateView):
    context_object_name = 'page'
    template_name = 'page3.html'

    def get_context_data(self, **kwargs):
        context = super(PageStyleThree, self).get_context_data(**kwargs)
        context['page'] = get_object_or_404(main.Page, type_page=kwargs['type_page'], slug=kwargs['slug'])
        context['category'] = \
            main.PageCategory.objects.filter(page__slug=kwargs['slug']).order_by('number')
        context['banners'] = \
            main.BannerPage.objects.filter(page__slug=kwargs['slug']).order_by('number')
        return context


class PageStyleFour(TemplateView):
    context_object_name = 'page'
    template_name = 'page4.html'

    def get_context_data(self, **kwargs):
        context = super(PageStyleFour, self).get_context_data(**kwargs)
        context['page'] = get_object_or_404(main.Page, type_page=kwargs['type_page'], slug=kwargs['slug'])
        context['category'] = \
            main.PageCategory.objects.filter(page__slug=kwargs['slug']).order_by('number')
        context['spoiler'] = \
            main.SpoilerPage.objects.filter(page__slug=kwargs['slug']).order_by('number')
        return context


class PageStyleFive(TemplateView):
    context_object_name = 'page'
    template_name = 'page5.html'

    def get_context_data(self, **kwargs):
        context = super(PageStyleFive, self).get_context_data(**kwargs)
        context['page'] = get_object_or_404(main.Page, type_page=kwargs['type_page'], slug=kwargs['slug'])
        context['category'] = \
            main.PageCategory.objects.filter(page__slug=kwargs['slug']).order_by('number')
        context['banners'] = \
            main.BannerPage.objects.filter(page__slug=kwargs['slug']).order_by('number')
        context['spoiler'] = \
            main.SpoilerPage.objects.filter(page__slug=kwargs['slug']).order_by('number')
        return context


class AllCategories(ListView):
    context_object_name = 'page'
    template_name = 'all-categories.html'
    queryset = main.PageCategory.objects.order_by('number')

