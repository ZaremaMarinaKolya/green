from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from . import models as main
from django.shortcuts import render


class About(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['page'] = get_object_or_404(main.AboutUs, slug = kwargs['slug'])

        context['team'] = main.Team.objects.filter(aboutus__slug=kwargs['slug']).order_by('number')
        context['customers'] = main.Customers.objects.filter(aboutus__slug=kwargs['slug']).order_by('number')
        return context


class Team(DetailView):
    queryset = main.Team.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'team.html'


class Customer(DetailView):
    queryset = main.Customers.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'customer.html'


class AllTeam(ListView):
    queryset = main.Team.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'all-team.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(AllTeam, self).get_context_data(**kwargs)
        context['about'] = main.AboutUs.objects.order_by('number')
        return context


def search(request):
    persons = ''
    if 'name' in request.GET and request.GET['name']:
        name = request.GET['name']
        persons = main.Team.objects.filter(name__icontains=name)
    return render(request, 'search.html', {'persons': persons})


class AboutCustomer(TemplateView):
    template_name = "about-customer.html"

    def get_context_data(self, **kwargs):
        context = super(AboutCustomer, self).get_context_data(**kwargs)
        context['page'] = get_object_or_404(main.AboutCustomer, slug = kwargs['slug'])

        context['team'] = main.Team.objects.filter(aboutcustomer__slug=kwargs['slug']).order_by('number')
        context['customers'] = main.Customers.objects.filter(aboutcustomer__slug=kwargs['slug']).order_by('number')
        return context


class AllCustomers(ListView):
    queryset = main.Customers.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'all-customers.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(AllCustomers, self).get_context_data(**kwargs)
        context['about'] = main.AboutCustomer.objects.order_by('number')
        return context


def search_customers(request):
    persons = ''
    if 'name' in request.GET and request.GET['name']:
        name = request.GET['name']
        persons = main.Customers.objects.filter(name__icontains=name)
    return render(request, 'search-customers.html', {'persons': persons})