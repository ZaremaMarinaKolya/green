from django.views.generic import DetailView, ListView
from . import models as main


class Image(DetailView):
    queryset = main.Gallery.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'image.html'


class GalleryOneCol(ListView):
    queryset = main.Gallery.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'gallery-1-col.html'
    paginate_by = 5


class GalleryTwoCol(ListView):
    queryset = main.Gallery.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'gallery-2-col.html'
    paginate_by = 6


class GalleryThreeCol(ListView):
    queryset = main.Gallery.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'gallery-3-col.html'
    paginate_by = 6


class GalleryFourCol(ListView):
    queryset = main.Gallery.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'gallery-4-col.html'
    paginate_by = 8
