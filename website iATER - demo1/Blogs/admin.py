from django.contrib import admin
from .models import Blogss

# Register your models here.
class Bigadmin(admin.ModelAdmin):
    list_display = ['blogs_TxtH']

    prepopulated_fields = {'slug':['blogs_TxtH']}

admin.site.register(Blogss,Bigadmin)
