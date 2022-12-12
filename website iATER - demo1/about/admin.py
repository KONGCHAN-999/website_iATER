from django.contrib import admin
from .models import About_head,About_services,About_service_img,About_Lab2

class Bigadmin(admin.ModelAdmin):
    list_display = ['d_txt1','show_service_pic']
class About_Lab_admin(admin.ModelAdmin):
    list_display = ['d_txt1','show_Lab_pic']

admin.site.register(About_head)
admin.site.register(About_services)
admin.site.register(About_service_img,Bigadmin)
admin.site.register(About_Lab2,About_Lab_admin)
