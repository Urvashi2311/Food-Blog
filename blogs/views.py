from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    post=Post.objects.all().filter().order_by('-add_date')[:5]
    #print(repost)
    data ={        
        'posts':post
    }
    return render(request,'index.html',data)

def HypothyroidDP(request):
    return render(request,"HypothyroidDP.html");

def DiabetesDP(request):
    return render(request,"DiabetesDP.html");

def GallBladderDP(request):
    return render(request,"GallBladderDP.html");

def gallery(request):
    return render(request,"gallery.html");

def vgallery(request):
    return render(request,"vgallery.html");

def carousal(request):
    return render(request,"carousal.html");


def blogCat(request):
       
    post=Post.objects.all().filter().order_by('-add_date')
    #print(post)
    data ={        
        'posts':post
    }
    return render(request,'blogCat.html',data)



def post(request,url):
    post=Post.objects.get(url=url)
    #print(post)
    data ={
        'post':post
    }
    return render(request,'post.html',data)

