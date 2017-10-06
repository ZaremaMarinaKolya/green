"""khu_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views as main


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^image/(?P<slug>[-\w]+)/$', main.Image.as_view(), name='image-detail'),
    url(r'^gallery-one-col/$', main.GalleryOneCol.as_view(), name='gallery-one-col'),
    url(r'^gallery-two-col/$', main.GalleryTwoCol.as_view(), name='gallery-two-col'),
    url(r'^gallery-three-col/$', main.GalleryThreeCol.as_view(), name='gallery-three-col'),
    url(r'^gallery-four-col/$', main.GalleryFourCol.as_view(), name='gallery-four-col'),

]

