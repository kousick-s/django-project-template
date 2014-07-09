from django.shortcuts import render
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render_to_response
from django import template
from todoapp.models import movie
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from logilab.common.compat import json
admin.autodiscover()
# Create your views here.

from django.http import HttpResponse

def index(request):
    return render_to_response('login.html')


def page1(request):
    return render_to_response('home.html')


def savetask(request,task_name):
    #name = request.POST['name']
    movieObject= movie(name=task_name)
    if movieObject:
        movieObject.save()
        movieObject= movie.objects.all()
        return render_to_response('home.html',{'pfields':movieObject})
    #else:
        #userprofile = UserProfiles(user=request.user, location=location, email=email)
        #userprofile.save()
        #return render_to_response('profile.html',{'pfields':userprofile})
        
def movies(request):
    #name = request.POST['name']
    movieObject= movie.objects.all()
    return render_to_response('home.html',{'pfields':movieObject})



def createuser(request,user_name):
     user = User.objects.create_user(user_name, 'lennon@thebeatles.com', user_name)
     if user:
         return render_to_response('signup.html',{'status':user})

@csrf_exempt
def authenticate_user(request):  
    print 'hapening',request.body
    data= json.loads(request.body)
    user_name = data.get('user_name')
    passw=data.get('passw')
    print user_name
    print passw
    #passw = request.POST['passw']
    user = authenticate(username=user_name, password=passw)
    if user is not None:
    # the password verified for the user
        if user.is_active:
            return HttpResponse('active')
        else:
            return HttpResponse('non-active')
    else:
    # the authentication system was unable to verify the username and password
        return("in-valid")   
     