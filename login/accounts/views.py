from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from .models import Post,Like,EditProfile
from .forms import ImageForm,EditForm
from django.urls import reverse_lazy , reverse
from django.http import HttpResponseRedirect



def like_post(request):
    user=request.user
    if request.method=='POST':
        post_id=request.POST.get('post_id')
        post_obj=Post.objects.get(id=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like,created=Like.objects.get_or_create(user=user,post_id=post_id)
        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
            like.save()                
    return redirect("viewpost")



def post_view(request):
    qs = Post.objects.all()
    user = request.user
    context = {
        'qs' : qs,
        'user' : user,
    }
    return render(request,'viewpost.html',context)

def addpostview(request):
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=ImageForm()
    return render(request,'addpost.html',{'form':form})

def edit_view(request):
    if request.method=="POST":
        form=EditForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=EditForm()
    return render(request,'editprofile.html',{'form':form})


def indexView(request):
    return render(request,'index.html')

def suggestions_view(request):
    return render(request,'suggestion.html')    

@login_required


def dashboardView(request):
    qs = Post.objects.all()
    obj=EditProfile.objects.all()
    return render(request,'dashboard.html',{'obj':obj,'qs':qs})

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else :
        form = UserCreationForm()      
    return render(request,'registration/register.html',{'form':form})    

