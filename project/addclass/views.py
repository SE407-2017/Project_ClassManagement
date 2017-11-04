# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from .models import Category, Course

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
    return render(request,
                  'coursepage/course/detail.html',
                  {'course': Course})

def search(request):
    q = request.GET.get('q')
    error_msg = ''
    
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'coursepage/course/list.html', {'error_msg': error_msg})

    course_list = Course.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'coursepage/course/search.html', {'error_msg': error_msg,
                  'course_list': course_list})
