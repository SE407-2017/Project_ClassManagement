from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='course_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.course_list,
        name='course_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.course_detail,
        name='course_detail'),
    url(r'^search/$', views.search, name='search'),
]
