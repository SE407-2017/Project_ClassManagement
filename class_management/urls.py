# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^regist/$',views.regist),
    url(r'^edit_product/$',views.edit_product),
    url(r'^$', views.course_list, name='course_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.course_list,
        name='course_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.course_detail,
        name='course_detail'),
    ]
'''
zhangzongrui and xiefei add the edit_product function
the function is used to edit the information of users
'''

'''
wyz add 课程信息界面所需url
‘’‘
