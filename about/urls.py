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
    url(r'^about/(?P<slug>[-\w]+)/$', main.About.as_view(), name='about'),
    url(r'^employee-detail/(?P<slug>[-\w]+)/$', main.Team.as_view(), name='employee-detail'),
    url(r'^customer-detail/(?P<slug>[-\w]+)/$', main.Customer.as_view(), name='customer-detail'),
    url(r'^about-customer/(?P<slug>[-\w]+)/$', main.AboutCustomer.as_view(), name='about-customer'),
    url(r'^all-team/$', main.AllTeam.as_view(), name='all-team'),
    url(r'^all-customers/$', main.AllCustomers.as_view(), name='all-customers'),
    url(r'^search/$', main.search, name='search'),
    url(r'^search-customers/$', main.search_customers, name='search-customers'),

]

