from django.contrib import admin

from blog.models import Contactus
from blog.models import store_name
# Register your models here.
admin.site.register(Contactus)
admin.site.register(store_name)