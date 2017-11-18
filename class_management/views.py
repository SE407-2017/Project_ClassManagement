# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django import forms
from models import theUser
from django.template import RequestContext, loader
from django.shortcuts import redirect



class UserFormForRegist(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')

class UserFormForLogin(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

class UserFormForedit(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')

def regist(request):
    if request.method == 'POST':
        userform = UserFormForRegist(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            newUser = theUser(user_name=username,user_password=password,user_email=email)
            newUser.save()

            return HttpResponse('regist success!!!')
    else:
        userform = UserFormForRegist()
    return render(request,'regist.html',{'userform':userform})######

def login(request):
    if request.method == 'POST':
        userform = UserFormForLogin(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = theUser.objects.filter(user_name__exact=username,user_password__exact=password)

            if user:
                return render(request,'index.html',{'userform':userform})
            else:
                return HttpResponse('用户名或密码错误,请重新登录')

    else:
        userform = UserFormForLogin()
    return render(request,'login.html',{'userform':userform})
def edit_product(request):
    if request.method == 'POST':
        userform = UserFormForedit(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            newUser = theUser(user_name=username,user_password=password,user_email=email)
            newUser.save()

            return HttpResponse('edit success!!!')
    else:
        userform = UserFormForedit()
    return render(request,'edit.html',{'userform':userform})######
'''
zhangzongrui and xiefei add the edit_product function and class UserFormForedit
the function is used to edit the information of users
'''

def course_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    courses = Course.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        courses = courses.filter(category=category)
    return render(request,
                  'user/course/list.html',
                  {'category': category,
                  'categories': categories,
                  'courses': courses})

def course_detail(request, id, slug):
    course = get_object_or_404(Course,
                               id=id,
                               slug=slug,
                               available=True)
    return render(request,
                  'user/course/detail.html',
                  {'course': course})
            

            
    
