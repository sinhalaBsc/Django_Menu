from django.conf.urls import url ,include
from django.views.generic import ListView , DetailView
from menu.models import mymenu
from django.urls import include ,path , re_path
from . import views


urlpatterns=[
    
    url(r'^$',ListView.as_view(queryset=mymenu.objects.all().order_by("-date")[:25],
                               template_name="menu/home.html")),
    
    re_path(r'(?P<url>(\w+))', views.get_select,name='get_select'),


    ]

