from django.shortcuts import render
from .models import Sw_head

# Create your views here.
def software(request):
    sw_head = Sw_head.objects.all()
    return render(request,'software.html',{
        'sw_head': sw_head
    })