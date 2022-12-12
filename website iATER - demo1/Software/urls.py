from django.urls import path
from . import views

urlpatterns = [
    path('software/',views.software, name='software'),

]