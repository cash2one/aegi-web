#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from order.forms import orderForm
from django.shortcuts import HttpResponseRedirect
import json
from order.models import *
from django.http import HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
# import the logging library
import logging
logger = logging.getLogger('django-error')


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
            #generate available
            myForm.save()
            paymethod = myForm.cleaned_data['paymentMethod']

            #generate out_trade_no
            out_trade_no = gen_trade_no()
            #calculate price
            number = int(myForm.cleaned_data['number'])
            haveKit = myForm.cleaned_data['haveKit']
            kitId = myForm.cleaned_data['kitId']
            price = 0
            if haveKit == '0':
                price = float(settings.YCBPRICE)*number
            else:
                productInfo = productModel.objects.filter(kitId=kitId)
                if len(productInfo):
                    price = float(productInfo[0].price)*number
                else:
                    price = float(settings.YCBPRICE)*number

            transaction = transactionModel(order = myForm.instance,price=price, out_trade_no=out_trade_no)
            transaction.save()

            if paymethod == 'alipay':
                url = '/order/payment/alipay'
            else:
                url = '/order/payment/wx'

            jsonData = {'url':url,'out_trade_no':out_trade_no}
            toJson = json.dumps(jsonData)
            return HttpResponse(toJson, content_type = "application/json")

    myForm = orderForm()
    return render(request, 'order/cart.html', {'myForm':myForm, 'languageCode':request.LANGUAGE_CODE})

# 下单页面校验kitid
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

#轮询检查是否成功,因为失败后我们无法得知是哪个订单是失败的,需要去微信查询当前订单是否支付成功,暂时简单处理,支付成功跳转,支付失败不做任何处理
def check_transaction(request):
    status = 0  #failed or not paied
    if request.method == 'POST' and 'trade_no' in request.POST:
        trade_no = request.POST['trade_no'].strip()
        transac = transactionModel.objects.filter(out_trade_no=trade_no)
        if len(transac):
            if transac[0].status == 1:
                status = 1

    jsonData = {'status':status}
    toJson = json.dumps(jsonData)
    return HttpResponse(toJson, content_type = "application/json")



def alipay(request):
    return render(request, 'order/alipay.html')

#weixin pay
from weixin import WeixinPay, WeixinPayError
from aegicare_web import settings
def wx(request):
    if request.method == 'GET' and 'trade_no' in request.GET:
        trade_no = request.GET['trade_no']
        transac = transactionModel.objects.filter(out_trade_no=trade_no)
        if len(transac) == 0:
            message = u'订单交易号不正确!'
            return_msg = ''
            return render(request, 'order/error.html',{'message':message,'return_msg':return_msg})
        else:
            appid = settings.appid
            mch_id = settings.mch_id
            mch_key = settings.mch_key
            notify_url = settings.notify_url
            spbill_create_ip = get_client_ip(request)
            pay = WeixinPay(appid, mch_id,mch_key, spbill_create_ip,notify_url)
            body = u"安吉康尔-Aegicare遗传病检测"
            trade_type = 'NATIVE'

            #get the total price
            total_fee = int(transac[0].price*100)

            try:
                raw = pay.unified_order(trade_type=trade_type, body=body, out_trade_no=trade_no, total_fee=total_fee, product_id=trade_no)
                if raw['return_code'] == 'SUCCESS':
                    if raw['result_code'] == 'SUCCESS':
                        prepay_id = raw['prepay_id']
                        code_url = raw['code_url']
                        return render(request, 'order/wx.html',{'code_url':code_url,'languageCode':request.LANGUAGE_CODE,'trade_no':trade_no})

                    else:
                        message = u'微信统一下单发生错误，请更改支付方式或者联系我们!'
                        return_msg = raw['err_code_des']
                        return render(request, 'order/error.html',{'message':message,'return_msg':return_msg})

                else:
                    message = u'微信统一下单发生错误，请更改支付方式或者联系我们!'
                    return_msg = raw['return_msg']
                    return render(request, 'order/error.html',{'message':message,'return_msg':return_msg})

            except WeixinPayError, e:
                print e.message

    return HttpResponseRedirect("/order/cart")

#notify_url
from util import *
from weixin import Map
@csrf_exempt
def wxCallback(request):
    message = 'FAIL'
    status = False
    if request.method == "POST":
        weixinRes = request.body.decode("utf-8")
        status = verifyNotice(weixinRes)
        if status == True:
            message = 'OK'
    return HttpResponse(reply(message,status))


def paySuccess(request):
    return render(request, 'order/paysuccess.html')


def verifyNotice(weixinRes):
    if len(weixinRes):
        data = Map(to_dict(weixinRes))
        if data.return_code == SUCCESS:
            if data.result_code == SUCCESS:
                #re sign
                weixin_sign = data.get('sign','')
                data.pop('sign', None)
                mch_key = settings.mch_key
                resign = sign(data,mch_key)
                if weixin_sign == resign:   #the sign is right
                    #check the total_fee is right
                    weixin_total_fee = int(data.total_fee)
                    weixin_out_trade_no = data.out_trade_no
                    transac = transactionModel.objects.filter(out_trade_no=weixin_out_trade_no)
                    if len(transac):
                        total_fee = int(transac[0].price*100)
                        if weixin_total_fee == total_fee:    #the price is right
                            #update the database
                            transactionModel.objects.filter(out_trade_no=weixin_out_trade_no).update(status=1)
                            return True

            else:
                logger.error(data.err_code_des)
        else:
            logger.error(data.return_msg)

    return False

#get client ip address for weixin pay
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
