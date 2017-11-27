# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^regist/$',views.regist),
    url(r'^edit_product/$',views.edit_product,name='edit_product'),
    
    ]
'''
zhangzongrui and xiefei add the edit_product function
the function is used to edit the information of users
'''

