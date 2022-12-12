from django.db import models
from django.utils.html import format_html

# Create your models here.

class About_head(models.Model):
    about_h = models.CharField(max_length=150)
    about_t = models.TextField()
    def __str__(self):
        return self.about_h
        
class About_services(models.Model):
    about_service_h = models.CharField(max_length=150)
    about_service_t1 = models.TextField()
    about_service_t2 = models.TextField()
    about_service_t3 = models.TextField()
    def __str__(self):
        return self.about_service_h

class About_service_img(models.Model):
    d_txt1 = models.TextField()
    image1 = models.ImageField(upload_to='media/media')
    d_txt2 = models.TextField()
    image2 = models.ImageField(upload_to='media/media')

    def show_service_pic(self):
        if self.image1:
            return format_html('<img src="%s" height="50px">' % self.image1.url)
        return 'NULL'
    show_service_pic.allow_tags = True

class About_Lab2(models.Model):
    h_txt1 = models.CharField(max_length=100)
    d_txt1 = models.TextField()
    image1 = models.ImageField(upload_to='media/media')
    h_txt2 = models.CharField(max_length=100)
    d_txt2 = models.TextField()
    image2 = models.ImageField(upload_to='media/media')

    def show_Lab_pic(self):
        if self.image1:
            return format_html('<img src="%s" height="50px">' % self.image1.url)
        return 'NULL'
    show_Lab_pic.allow_tags = True