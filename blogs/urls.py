
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from blogs import views

urlpatterns = [
    path('blogCat/',views.blogCat,name="BlogCat"),
    path('blogs/<slug:url>',views.post)
] 