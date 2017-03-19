from django.shortcuts import render
from order.forms import orderForm
from django.shortcuts import HttpResponseRedirect
import json
from order.models import *
from django.http import HttpResponse
import datetime

# Create your views here.
def order(request):
    return render(request, 'order/order.html')

# set cookie for the cart page
def set_cookie(response, key, value, days_expire = 7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  #one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires)


def cart(request):
    if request.method == 'POST':
        myForm = orderForm(request.POST)
        if myForm.is_valid():
            myForm.save()
            paymethod = myForm.cleaned_data['paymentMethod']
            if paymethod == 'alipay':
                url = '/order/payment/alipay'
            else:
                url = '/order/payment/wx'

            jsonData = {'url':url}
            toJson = json.dumps(jsonData)
            return HttpResponse(toJson, content_type = "application/json")

    myForm = orderForm()
    return render(request, 'order/cart.html', {'myForm':myForm, 'languageCode':request.LANGUAGE_CODE})


def validateKit(request):
    price = 0
    status = 0
    if request.method == 'GET':
        kitid = request.GET.get('kitid',0)
        result = productModel.objects.filter(kitId= kitid)
        if len(result):
            price = result[0].price
            status = 1

    jsonData = {'status':status,'price':price}
    toJson = json.dumps(jsonData)
    return HttpResponse(toJson, content_type = "application/json")


def alipay(request):
    return render(request, 'order/alipay.html')

def wx(request):
    return render(request, 'order/wx.html')