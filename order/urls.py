from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.order, name='order'),
    url(r'^cart', views.cart, name='cart'),
    url(r'^validateKit$',views.validateKit,name='validateKit'),
    url(r'^ajax/check_transaction$',views.check_transaction,name='check_transaction'),
    url(r'^payment/alipay$', views.alipay, name='alipay'),
    url(r'^payment/wx$', views.wx, name='wx'),
    url(r'^payment/wx/callback$', views.wxCallback, name='wxCallback'),
    url(r'^payment/success', views.paySuccess, name='paySuccess'),
]