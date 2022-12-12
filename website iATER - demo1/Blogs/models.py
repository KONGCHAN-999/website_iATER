from django.db import models
from django.utils.html import format_html

# Create your models here.

class Blogss(models.Model):
    blogs_TxtH = models.CharField(max_length=150, unique=True)
    blogs_Txt = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    blogs_Image = models.ImageField(upload_to='media/media')

    def show_service_pic(self):
        if self.blogs_Image:
            return format_html('<img src="%s" height="50px">' % self.blogs_Image.url)
        return 'NULL'
    show_service_pic.allow_tags = True