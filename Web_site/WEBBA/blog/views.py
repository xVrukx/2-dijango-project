from django.shortcuts import render

from blog.models import Contactus
from blog.models import store_name
# Create your views here.
def blog (request):

    data = {"name":"Yuvraj","lastname":"sirganor"}


    return render(request,'BLOG.html',context=data)

def contactUs_data(request):
    data = Contactus.objects.all()[::-1]
    return render(request,'allData.html',context={"data":data})

def store(request):
    name = store_name.objects.all()[::1]
    return render(request,'storeht.html', context={'name':name})
