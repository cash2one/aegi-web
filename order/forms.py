#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.forms import ModelForm,RadioSelect,ChoiceField,NumberInput
from order.models import *

# Create your models here.
class orderForm(ModelForm):
    province = ChoiceField()
    city = ChoiceField()
    county = ChoiceField()

    class Meta:
        model = orderModel
        fields = ('number', 'haveKit','kitId','username','email','phone','province','city','county','address','paymentMethod','radioInvoice','invoice','message')

        widgets = {
            'number':NumberInput(attrs={'min': 1}),
            'haveKit': RadioSelect(),
            'paymentMethod': RadioSelect(),
            'radioInvoice':RadioSelect(),
        }

        def clean_kitId(self):  #allow empty for kitId
            return self.cleaned_data['kitId'] or None

        help_texts = {
            'username': 'Some useful help text.',
        }

        error_messages = {
            'username':{
                'required':u'请输入联系人姓名',
                'invalid': u'请输入正确的联系人姓名'
            },
            'email': {
                'required':u'需要输入邮箱',
                'invalid': u'请提供有效的邮箱地址'
            },

        }

    def __init__(self, *args, **kwargs):
        super(orderForm,self).__init__(*args, **kwargs)
        self.fields['kitId'].widget.attrs.update({
            'placeholder': '采集管编码',
            'class': 'form-control',
        })

        self.fields['number'].widget.attrs.update({
            'class': 'mui-input-numbox',
        })




        self.fields['username'].widget.attrs.update({
            'placeholder': '请输入联系人姓名',
            'class': 'form-control',
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': '请输入您正确的邮箱',
            'class': 'form-control',

        })

        self.fields['phone'].widget.attrs.update({
            'placeholder': '请输入您的手机号码',
            'class': 'form-control',
        })

        self.fields['province'].widget.attrs.update({
            'class': 'selectAddress',
        })

        self.fields['city'].widget.attrs.update({
            'class': 'selectAddress',
        })

        self.fields['county'].widget.attrs.update({
            'class': 'selectAddress',
        })

        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder':'请输入您详细的地址',
        })

        self.fields['paymentMethod'].widget.attrs.update({
            'class': 'hide',
        })

        self.fields['message'].widget.attrs.update({
            'placeholder':'选填',
            'class': 'form-control',
        })










