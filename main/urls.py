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
from django.conf.urls import url, include
from . import views as main


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', main.Home.as_view(), name='index'),
    url(r'^category/(?P<slug>[-\w]+)/$', main.PageCategory.as_view(), name='page-category'),
    url(r'^all-categories/$', main.AllCategories.as_view(), name='all-categories'),
    url(r'^page/(?P<type_page>style-one)/(?P<slug>[-\w]+)/$', main.PageStyleOne.as_view(), name='page-style-one'),
    url(r'^page/(?P<type_page>style-two)/(?P<slug>[-\w]+)/$', main.PageStyleTwo.as_view(), name='page-style-two'),
    url(r'^page/(?P<type_page>style-three)/(?P<slug>[-\w]+)/$', main.PageStyleThree.as_view(), name='page-style-three'),
    url(r'^page/(?P<type_page>style-four)/(?P<slug>[-\w]+)/$', main.PageStyleFour.as_view(), name='page-style-four'),
    url(r'^page/(?P<type_page>style-five)/(?P<slug>[-\w]+)/$', main.PageStyleFive.as_view(), name='page-style-five'),
    url(r'^contact/(?P<slug>[-\w]+)/$', main.contact, name='contact-detail'),
    url(r'^thanks', main.thanks, name='thanks'),

]

