from django.shortcuts import render 
from .models import mymenu


def get_select(request , url):
    instance=mymenu.objects.filter(url=url)
    Menu=mymenu.objects.all().order_by("-date")
    context={
        "select_url":instance,
        "url":"List",
        "menu":Menu
        }
    return render(request,'menu/page.html',context)
