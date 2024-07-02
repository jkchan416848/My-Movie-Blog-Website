from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from app_movie.views import intro_view,main_movie_page_view
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.core.mail import send_mail
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Enter Username...'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Enter Password...'}))

def Register_form_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            pass_word = form.password
            form.password = make_password(pass_word)
            Email_Send_From = settings.EMAIL_HOST_USER
            Recipient_List = [form.email,]
            Subject = 'Welcome to My Jk-Blog site'
            Message = f'Dear, {form.username}, Thanks for Register jk-Blog website'
            send_mail(Subject,Message,Email_Send_From,Recipient_List)
            form.save()
            return log_in_view(request)
    context = {'form':form}   
    return render(request,'user_register.html',context) 

def log_in_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password= password)
        if user is not None:
            login(request,user)
            return intro_view(request)
    context = {'form':form}    
    return render(request,'login.html',context)


@login_required(login_url='/login/')
def log_out_view(request):
    logout(request)
    return main_movie_page_view(request)

def conform_view(request):
    request.user.is_authenticate()
    print(request.user)
    return render(request,'navigation.html')
