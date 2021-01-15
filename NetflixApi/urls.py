from django.urls import include,path,re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    url(r'^youtube/(\d+)',views.youtube,name = 'youtube')
]