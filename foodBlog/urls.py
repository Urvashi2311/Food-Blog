
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from blogs import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),       
    path('blogCat/',views.blogCat,name='BlogCat'),   
    path('blogs/<slug:url>',views.post),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

