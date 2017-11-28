# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from .models import Category, Course
from class_management.models import theUser


def course_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    courses = Course.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        courses = courses.filter(category=category)
    return render(request,
                  'coursepage/course/list.html',
                  {'category': category,
                  'categories': categories,
                  'courses': courses})

def course_detail(request, id, slug):
    course = get_object_or_404(Course,
                                id=id,
                                slug=slug,
                                available=True)
    request.session['course'] = course.id
    return render(request,
                  'coursepage/course/detail.html',
                  {'course': course})

def search(request):
    q = request.GET.get('q')
    error_msg = ''
    
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'course/list.html', {'error_msg': error_msg})

    course_list = Course.objects.filter(title__icontains=q)
    return render(request, 'coursepage/list.html', {'error_msg': error_msg,
                  'course_list': course_list})

def choose(request):
    thisCourse = Course.objects.get(id = request.session.get('course'))
    User = theUser.objects.get(user_name = request.session.get('User'))
    User.course_list.add(thisCourse)
    User.save()
    return render(request,
                  'coursepage/course/detail.html',
                  {'course': thisCourse})
