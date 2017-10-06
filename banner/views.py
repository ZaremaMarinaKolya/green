from django.views.generic import DetailView, ListView
from . import models as main


class BannerOne(DetailView):
    queryset = main.BannerOne.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'banner.html'


class BannerOneList(ListView):
    queryset = main.BannerOne.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'banner-one-list.html'
    paginate_by = 5


class BannerTwo(DetailView):
    queryset = main.BannerTwo.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'banner.html'


class BannerTwoList(ListView):
    queryset = main.BannerTwo.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'banner-two-list.html'
    paginate_by = 5


class BannerThree(DetailView):
    queryset = main.BannerThree.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'banner.html'


class BannerThreeList(ListView):
    queryset = main.BannerThree.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'banner-three-list.html'
    paginate_by = 5


class BannerPage(DetailView):
    queryset = main.BannerPage.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'banner.html'

