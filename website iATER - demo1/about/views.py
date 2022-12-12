from django.shortcuts import render
from .models import About_head,About_services,About_service_img,About_Lab2

# Create your views here.
def about(request):
    about_head = About_head.objects.all()
    about_service = About_services.objects.all()
    about_service_img = About_service_img.objects.all()
    about_Lab = About_Lab2.objects.all()
    return render(request,'about.html',{
        'about_head':about_head,
        'about_service':about_service,
        'about_service_img':about_service_img,
        'about_Lab':about_Lab,
    })