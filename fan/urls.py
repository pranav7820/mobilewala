from django.contrib import admin
from django.urls import path
from . import views
admin.site.site_header = "Pranav ki School"
admin.site.site_title = "Pranav is the best"
admin.site.index_title = "Welcome to Pnna Worlds"

urlpatterns = [
    path('',views.index,name='index'),
    path('python/',views.python,name='python'),
    path('html/',views.html,name='html'),
    path('css/',views.css,name='css'),
    path('java/',views.java,name='java'),
    path('contact/',views.contact,name='contact'),
    path('link/',views.link,name='link'),
]