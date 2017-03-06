from django.conf.urls import url
from . import views
app_name = 'news'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
]