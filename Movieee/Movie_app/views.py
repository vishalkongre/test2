from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.sessions.models import Session
from django.db import connection
from django.core.mail import send_mail
from Movieee import settings

# Create your views here.
def showdata(request):
    if request.session.has_key('logged_in'):
        all_movies = MovieInfo.objects.filter(userid=request.session['userid'])
        return render(request, "showdata.html",{'Movies' : all_movies })
    else:
        return redirect('index')

def AddMovie(request):
    return render(request,"add_movie.html")

def add_movie_submission(request):
    print ("hello form is submitted.")
    movie_name = request.POST["movie_name"]
    movie_type = request.POST["movie_type"]
    movie_review = request.POST["movie_review"]
    movie_release = request.POST["movie_release"]
    movie_detail = request.POST["movie_detail"]
    userid = request.session['userid']

    movie_info = MovieInfo(movie_name=movie_name,movie_type=movie_type,movie_review=movie_review,movie_release=movie_release,movie_detail=movie_detail)
    movie_info.userid_id=userid
    movie_info.save()
    messages.success(request,'The form was successfully submitted.')
    return render(request, "add_movie.html")

def Register(request):
    return render(request,"register.html")
    

def register_submission(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username Taken')
                print('username')
                return render(request,"register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                print('email')
                return render(request,"register.html")
            elif send_mail('Hello from Movie Info','welcome to our website.\n Username : '+username+'\n Password : '+password1+'','vkongre92@gmail.com',[email]):
                user = User(username = username, password=password1,email=email,fname=first_name,lname=last_name)   
                user.save();
                messages.info(request,'User Created')
                return redirect('index')

            else:
                messages.info(request,'oops...!somthing went wrong!!!!')
                return render(request, "register.html")
        else:
            messages.info(request,'Password not Maching')

            return render(request,"register.html")

    else:
        return render (request,"register.html")

def index(request):
    if request.session.has_key('logged_in'):
        return redirect('showdata')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        
        count = User.objects.filter(username=username,password=password).count()
        if count>0 : 
            request.session['logged_in']=True
            request.session['userid']=User.objects.values('id').filter(username=username,password=password)[0]['id']
            return redirect('showdata')

        else:
            messages.info(request,'Invalide credentials')
            return redirect('index') 

    else:
        return render( request ,"index.html")

def logout(request):
    del request.session['logged_in']
    return redirect('index')
