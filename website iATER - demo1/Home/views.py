from django.shortcuts import render
from .models import Text_head,Txt_wwr,Img_home,Txt_foot

# Create your views here.

def home(request):
    news = Text_head.objects.all()
    txt_wwr = Txt_wwr.objects.all()
    img_home = Img_home.objects.all()
    txt_foot = Txt_foot.objects.all()
    return render(request,'home.html',{
        'news':news,
        'txt_wwr':txt_wwr,
        'img_home':img_home,
        'txt_foot':txt_foot,
    })


def login(request):
    return render(request,'login.html')
def chat(request):
    return render(request,'chat.html')
    

