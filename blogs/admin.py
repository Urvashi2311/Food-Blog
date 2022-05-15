from django.contrib import admin
from blogs.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display =('image_tag','title','add_date')
    search_fields = ('title',)    
    list_per_page=15

# Register your models here.

admin.site.register(Post,PostAdmin)
