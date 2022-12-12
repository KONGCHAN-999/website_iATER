from django.db import models
from django.utils.html import format_html

# Create your models here.
class Sw_head(models.Model):
    sw_h = models.CharField(max_length=150)
    sw_t = models.TextField()
    def __str__(self):
        return self.sw_h

class Sw_txtbody1_img(models.Model):
    bd_h_txt1 = models.TextField()
    bd_txt1 = models.TextField()
    image1 = models.ImageField(upload_to='media/media')

    def show_service_pic(self):
        if self.image1:
            return format_html('<img src="%s" height="50px">' % self.image1.url)
        return 'NULL'
    show_service_pic.allow_tags = True

class Sw_txtbody2_img(models.Model):
    bd_h_txt1 = models.TextField()
    bd_txt1 = models.TextField()
    image1 = models.ImageField(upload_to='media/media')

    def show_service_pic(self):
        if self.image1:
            return format_html('<img src="%s" height="50px">' % self.image1.url)
        return 'NULL'
    show_service_pic.allow_tags = True