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
    url(r'^banner-one/(?P<slug>[-\w]+)/$', main.BannerOne.as_view(), name='banner-one-detail'),
    url(r'^banner-one-list/$', main.BannerOneList.as_view(), name='banner-one-list'),
    url(r'^banner-two/(?P<slug>[-\w]+)/$', main.BannerTwo.as_view(), name='banner-two-detail'),
    url(r'^banner-two-list/$', main.BannerTwoList.as_view(), name='banner-two-list'),
    url(r'^banner-three/(?P<slug>[-\w]+)/$', main.BannerThree.as_view(), name='banner-three-detail'),
    url(r'^banner-three-list/$', main.BannerThreeList.as_view(), name='banner-three-list'),
    url(r'^banner-page/(?P<slug>[-\w]+)/$', main.BannerPage.as_view(), name='banner-page-detail'),


]

