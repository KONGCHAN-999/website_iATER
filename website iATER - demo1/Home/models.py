
from distutils.command.upload import upload
from django.db import models
from django.utils.html import format_html

# Create your models here.

class Text_head(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title

class Txt_wwr(models.Model):
    t_head = models.CharField(max_length=200)
    d_txt = models.TextField()
    def __str__(self):
        return self.t_head

class Img_home(models.Model):
    image = models.ImageField(upload_to='media/media')
   
    def show_profile_pic(self):
        if self.image:
            return format_html('<img src="%s" height="50px">' % self.image.url)
        return 'NULL'
    show_profile_pic.allow_tags = True


class Txt_foot(models.Model):
    t_foot = models.CharField(max_length=150)
    d_txt1 = models.TextField()
    d_txt2 = models.TextField()
    d_txt3 = models.TextField()
    def __str__(self):
        return self.t_foot



# class Text_head(models.Model):
#     title = models.CharField(max_length=100)
#     desc = models.TextField()

#     def show_profile_pic(self):
#         if self.image:
#             return format_html('<img src="%s" height="50px">' % self.image.url)
#         return 'NULL'
#     show_profile_pic.allow_tags = True
#     def __str__(self):
#         return self.title
