"""aegicare_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView
from filebrowser.sites import site
import views

# urlpatterns = [
#     url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
#         home_files, name='home-files'),
# ]

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
]

urlpatterns += i18n_patterns(
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include('smuggler.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomePage, name='home'),
    url(r'^about$', views.About, name='about'),
    url(r'^service/genetic$', views.geneticInfo, name='geneticInfo'),
    url(r'^service/cancer$', views.cancerInfo, name='cancerInfo'),
    url(r'^service/cdss$', views.cdss, name='cdss'),
    url(r'^career/$', views.career, name='career'),
    url(r'^team/$', views.team, name='team'),
    url(r'^report/$', views.report, name='report'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^workflow/$', views.workflow, name='workflow'),
    url(r'^mission/$', views.mission, name='mission'),
    url(r'^order/', include('order.urls', namespace="order")),
    url(r'^news/', include('news.urls', namespace="news")),
    url(r'^accounts/', include('allauth.urls')),
)
