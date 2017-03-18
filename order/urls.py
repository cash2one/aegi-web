from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.order, name='order'),
    url(r'^pay$', views.pay, name='pay'),
]