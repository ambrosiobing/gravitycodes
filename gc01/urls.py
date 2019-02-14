"""gc01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_gravcode.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
Definition of urls for.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import gravcode.forms
import gravcode.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', gravcode.views.home, name='home'),
    url(r'^about', gravcode.views.about, name='about'),
    url(r'^team', gravcode.views.team, name='team'),
    url(r'^services', gravcode.views.services, name='services'),
    url(r'^contact', gravcode.views.contact, name='contact'),
    url(r'^login',
        django.contrib.auth.views.login,
        {
            'template_name': 'gravcode/login.html',
            'authentication_form': gravcode.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

