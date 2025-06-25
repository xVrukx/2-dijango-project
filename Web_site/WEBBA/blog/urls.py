from django.urls import path
from .views import *

urlpatterns = [
    path('',blog, name = "Blog"),
    path('contactUs_data/',contactUs_data, name = "contactUs_data"),
    path('store/',store, name='Store')
]