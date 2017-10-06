from django.views.generic import DetailView, ListView
from . import models as main


class News(DetailView):
    queryset = main.News.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'news.html'


class AllNews(ListView):
    queryset = main.News.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'news-list.html'
    paginate_by = 5


class Opinion(DetailView):
    queryset = main.Opinion.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'opinion.html'


class AllOpinions(ListView):
    queryset = main.Opinion.objects.order_by('number')
    context_object_name = 'page'
    template_name = 'opinions-list.html'
    paginate_by = 5

