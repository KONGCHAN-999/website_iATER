from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blogss
# Create your views here.

def blogs(request):
    blogs = Blogss.objects.all()

    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.nim_pages)
    
    return render(request,'blogs.html',{
        'blogs': blogs
    })
    
def blogInfor(request, slug):
    blog = get_object_or_404(Blogss, slug=slug)
    return render(request,'blogInfor.html',{
        'blog': blog
    })
    