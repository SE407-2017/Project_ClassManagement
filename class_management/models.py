# -*- coding: utf-8 -*-
# by lvjun

from __future__ import unicode_literals
from django.db import models


class Course(models.Model):
    Course_name = models.CharField(max_length=200)
    SEMESTER_CHOICES = (('7F', '2017Fall'),
                        ('7U', '2017Summer'),
                        ('8S', '2018Spring')
                        )
    Course_semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES, default='7F')
    SCHOOL_CHOICE = (('SEIEE', 'School of Electronic Information and Electrical Engineering'),
                     # to be continued
                     )
    Course_student = models.CharField(max_length=10, choices=SCHOOL_CHOICE, default='SEIEE')
    Course_introduction = models.CharField(max_length=1000, default="The lazy gay leave nothing there.")

    def __str__(self):
        return self.Course_name
    # to be continued


class theUser(models.Model):
    user_name = models.CharField(max_length=15)
    user_password = models.CharField(max_length=20)
    USER_CHOICES = (('S', 'student'),
                    ('T', 'teacher')
                    )
    user_type = models.CharField(max_length=1, choices=USER_CHOICES, default='S')
    user_email = models.EmailField()
    user_course = models.ManyToManyField(Course)

    def __str__(self):
        return self.user_name
    #to be continued


#class Homework(models.Model):
#if needed

#somemore models to be continued
