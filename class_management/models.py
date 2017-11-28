# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from addclass.models import Course, Category

# Create your models here.

class theUser(models.Model):
    user_name = models.CharField(max_length=15)
    user_password = models.CharField(max_length=20)
    USER_CHOICES = (('S', 'student'),
                    ('T', 'teacher')
                    )
    user_type = models.CharField(max_length=1, choices=USER_CHOICES, default='S')
    user_email = models.EmailField()
    user_course = models.ManyToManyField(Course,blank=True)
    
    def __str__(self):
        return self.user_name

    def user_course_list(self):
            return ','.join([i.name for i in self.user_course.all()])
#to be continued
