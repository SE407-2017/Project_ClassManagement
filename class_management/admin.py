# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import theUser
from addclass.models import Course, Category

class theUserAdmin(admin.ModelAdmin):
    list_display = ['id','user_name','user_email','user_course_list']
admin.site.register(theUser,theUserAdmin)
