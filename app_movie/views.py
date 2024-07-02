from django.shortcuts import render
from .forms import Movie_Blog_form,Comment_form
from django.http import HttpResponse
from .models import Movie_Blog_Model,CommentModel
import random
from random import shuffle
from django.contrib.auth.decorators import login_required

def main_movie_page_view(request):
     data = list(Movie_Blog_Model.objects.all())
     rand_img = list(Movie_Blog_Model.objects.all())
     shuffle(data)
     recent_random = random.sample(rand_img,1)
     context = {"data":data,'rand_img':recent_random}
     return render(request,'main.html',context)

def Movie_review_page_view(request):
    if request.method == 'POST':
        name =  request.POST['get_movie']
        search_movies = Movie_Blog_Model.objects.filter(Movie_Title__contains=name)
        return render(request,'review.html',{'name':search_movies})
    else:
        data = Movie_Blog_Model.objects.latest('Movie_Review_on')
        context = {"data":data}
        return render(request,'review.html',context)

@login_required(login_url='login')
def About_page_view(request):
    data = Movie_Blog_Model.objects.all()
    context = {"data":data}
    return render(request,'about.html',context)

@login_required(login_url='login')
def Contact_page_view(request):
    return render(request,'contect.html')

def home_page_view(request):
    data = Movie_Blog_Model.objects.all()
    context = {"data":data,}
    return render(request,'home.html',context)

def Upload_img_blog_view(request):
    form = Movie_Blog_form()
    if request.method =="POST":
        form = Movie_Blog_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Movie Upload")
    context = {'form':form}
    return render(request,'upload_imgblog.html',context)

def Navigation_page_view(request): 
        return render(request,'navigation.html')

@login_required(login_url='login')
def Full_details_View(request,id):
    data = Movie_Blog_Model.objects.get(id=id)
    if request.method == "POST":
        cmt_form = Comment_form(request.POST)
        if cmt_form.is_valid():
            cmt_form.save()
    cmt_form = Comment_form(initial={"Movie_name":id,'User_name':request.user})
    comments = CommentModel.objects.filter(Movie_name=id)
    context = {"data":data,'cmt_form':cmt_form,'comments':comments} 
    return render(request,'full_details.html',context)

def Trailer_view(request):
    if request.method == 'POST':
        name =  request.POST['get_movie_trailer']
        search_movies = Movie_Blog_Model.objects.filter(Movie_Title__contains=name)
        return render(request,'trailer.html',{'search':search_movies})
    else:
        data = Movie_Blog_Model.objects.latest('Movie_Review_on')
        context = {'data':data}
        return render(request,'trailer.html',context)

def intro_view(request):
    return render(request,'intro.html')

