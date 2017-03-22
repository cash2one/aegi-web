#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

haveKit_choices = (
    ('0', '否'),
    ('1', '是'),)

payment_choices = (
    ('wx', '微信'),
    ('alipay', '支付宝'),
)

invoice_choices = (
    ('1', '不需要'),
    ('2', '个人'),
    ('3', '公司'),
)

#validator
def validate_province(value):
    if value == "省份":
        raise ValidationError(
                _('%(value)s 不是一个有效的省'),
                params={'value': value},
        )


def validate_city(value):
    if value == "地级市":
        raise ValidationError(
                _('%(value)s 不是一个有效的地级市'),
                params={'value': value},
        )


def validate_county(value):
    if value == "市、县级市":
        raise ValidationError(
                _('%(value)s 不是一个有效的市、县级市'),
                params={'value': value},
        )


# Create your models here.
class orderModel(models.Model):
    # product info
    number = models.IntegerField(default=1)
    haveKit = models.CharField(max_length=1, choices=haveKit_choices, default='0')
    kitId = models.CharField(max_length=10, blank=True,null=True)

    # customer info
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    province = models.CharField(max_length=20, validators=[validate_province])
    city = models.CharField(max_length=100,validators=[validate_city])
    county = models.CharField(max_length=100,validators=[validate_county])
    address = models.CharField(max_length=100)

    # payment info
    paymentMethod = models.CharField(max_length=10, choices=payment_choices, default='wx')
    radioInvoice = models.CharField(max_length=2, choices=invoice_choices, default='1')
    invoice = models.CharField(max_length=50, blank=True)
    message = models.CharField(max_length=255, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.number)+" "+self.email+" "+self.phone+" "+self.paymentMethod

#generate a transaction for pay
class transactionModel(models.Model):
    order = models.OneToOneField(orderModel)
    out_trade_no = models.CharField(max_length=30)
    price = models.FloatField(default=0)   #price
    status = models.IntegerField(default=0)  #1 success

    def __str__(self):              # __unicode__ on Python 2
        return self.out_trade_no


class productModel(models.Model):
    kitId = models.CharField(max_length=12,unique=True,default="1111000000")
    price = models.FloatField()
    status = models.IntegerField(default=0)  #0未使用; 1已下单未支付; 2已支付; 3已寄出(从医生处不需要寄送); 4已注册绑定采集管; 5采集管回到公司; 6采集管到测序公司; 7收到测序数据; 8产生报告

    def __str__(self):              # __unicode__ on Python 2
        return self.kitId + " " + str(self.price)+ " " + str(self.status)