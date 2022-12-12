from django.contrib import admin
from .models import Text_head,Txt_wwr,Img_home,Txt_foot

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','desc']
    search_fields = ['title']
    list_filter = ['title']


# Register your models here.

admin.site.register(Text_head, BlogAdmin)
admin.site.register(Txt_wwr)
admin.site.register(Img_home)
admin.site.register(Txt_foot)

