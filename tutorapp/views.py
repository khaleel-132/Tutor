from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template,loader
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *


# Create your views here.


def index(request):
    return render(request,'home/index.html')

def profile(request):
    if request.method == 'POST':
        qual = request.POST['qualification']
        uni = request.POST['university']
        col = request.POST['college']
        sch = request.POST['school']
        add = request.POST['address']
        role = request.POST['role']
        gen = request.POST['gender']
        user = Profile(qualification=qual,university=uni,college=col,school=sch,address=add,role=role,gender=gen)
        user.save()
        print(qual)
    return render(request,'home/profile.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None :
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'authentication/login.html')
def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return render(request,'authentication/signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return render(request,'authentication/signup.html')
            else :
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password1)
                user.save()
        else:
            messages.info(request,'Password Missmatch')
            return render(request,'authentication/signup.html')
        return redirect('login')
    else :
        return render(request,'authentication/signup.html')
    # return render(request,'authentication/signup.html')
def home(request):
    if request.method == 'POST':
        category = request.POST['category']
        clas = request.POST['class']
        sub = request.POST['subject']
        city = request.POST['city']
        place = request.POST['place']
        detail = request.POST['detail']
        gender = request.POST['gender']
        number = request.POST['no']
        salary = request.POST['salary']
        title = request.POST['post']
        phone = request.POST['phone']

        post = Post(category=category,clas=clas,subject=sub,city=city,place=place,place_detail=detail,gender=gender,no_student=number,salary=salary,title=title,phone=phone)
        post.save()
    posts = Post.objects.all()
    return render(request,'home/home.html',{'userpost':posts})
def logout(request):
    auth.logout(request)
    return redirect('index')

