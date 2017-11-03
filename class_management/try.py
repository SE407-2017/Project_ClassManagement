# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django import forms
from models import theUser

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
        userform = UserFormForedit(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email=userform.cleaned_data['email']
            
            newUser = theUser(user_name=username,user_password=password,user_email=email)
            newUser.save()
            return HttpResponse('good')
    if request.method == "GET":
        userform = UserFormForedit(initial={
                'username':username,
                'password':password,
                'email':email,
        }
        return render(request,'edit.html',{'userform':userform})
def edit_product(request):
    aler=u"提示："
    userform = UserFormForRegist(request.POST)
    stulist = theUser.objects.all()
    message=request.POST.get('message')
    old = request.POST.get('old')
    new=request.POST.get('new')
    username=request.POST.get('username')
    password=request.POST.get('password')
    email=request.POST.get('email')
    if old=='username':
        student=theUser.objects.filter(name_contains=message).update(username=new)
    elif old=='password':
        student=theUser.objects.filter(name_contains=message).update(password=new)
    elif old=='email':
        student=theUser.objects.filter(name_contains=message).update(email=new)
    else:
        aler+=u"请输入需要修改的："
    return render_to_response("edit.html",context_instance=RequestContext(request,{"message":message,"new":new,"stulist":stulist,"aler":aler)
