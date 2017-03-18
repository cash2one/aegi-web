#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator

haveKit_choices = (
('0', '否'),
('1', '是'),)

payment_choices = (
    ('wx','微信'),
    ('alipay','支付宝'),
)

invoice_choices = (
    ('1','不需要'),
    ('2','个人'),
    ('3','公司'),
)

# Create your models here.
class orderModel(models.Model):
    #product info
    number = models.IntegerField(default=1)
    haveKit = models.CharField(max_length=1,choices=haveKit_choices,default='0')
    kitId = models.CharField(max_length=10,blank = True,null = True,unique=True)

    #customer info
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    #payment info
    paymentMethod = models.CharField(max_length=10,choices=payment_choices,default='wx')
    radioInvoice = models.CharField(max_length=2,choices=invoice_choices,default='1')
    invoice = models.CharField(max_length=50)
    message = models.CharField(max_length=255,blank=True)







