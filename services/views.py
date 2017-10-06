from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from . import models as main
# Create your views here.


class Services(TemplateView):
    template_name = "services.html"
    queryset = main.Service.objects.order_by('number')
    context_object_name = 'page'


class ServicesDetail(DetailView):
    template_name = "service.html"
    queryset = main.Service.objects.order_by('number')
    context_object_name = 'page'


class ServicesList(ListView):
    template_name = "services-list.html"
    queryset = main.Service.objects.order_by('number')
    context_object_name = 'page'
    paginate_by = 5
