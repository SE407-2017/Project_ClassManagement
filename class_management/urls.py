# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.login),
    url(r'^regist/$',views.regist),
    url(r'^edit_product/$',views.edit_product),
    url(r'^course/$', views.course_list, name='course_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.course_list,
        name='course_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.course_detail,
        name='course_detail'),
    ]

