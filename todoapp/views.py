from django.shortcuts import render
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render_to_response
from django import template
from todoapp.models import movie
from todoapp.models import Task
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from logilab.common.compat import json
from django.db.models import Q
admin.autodiscover()
# Create your views here.

from django.http import HttpResponse

def index(request):
    return render_to_response('login.html')


def page1(request):
    return render_to_response('home.html')

@csrf_exempt
def save_task(request,user_id):
    data= json.loads(request.body)
    tTitledata = data.get('tTitle')
    tDescdata=data.get('tDesc')
    tStatusdata = data.get('tStatus')
    tAccessdata=data.get('tAccess')
    print tAccessdata
    userObject=User.objects.get(id=user_id)
    taskObject= Task(user=userObject, tTitle=tTitledata, tDesc=tDescdata, tStatus=tStatusdata, tAccess=tAccessdata)
    if taskObject:
        taskObject.save()
        return tasks(request,user_id)
   
        
def tasks(request,user_id):
    userObject=User.objects.get(id=user_id)
    taskObjectPending= Task.objects.filter(user=userObject,tStatus="Pending")
    taskObjectCompleted=Task.objects.filter(user=userObject,tStatus="Completed")
    taskObjectPublic=Task.objects.filter(~Q(user=userObject),tAccess="public")
    return render_to_response('home.html',{'completedtasks':taskObjectCompleted,'pendingtasks':taskObjectPending,'u_id':user_id,'publictasks':taskObjectPublic})


def create_user(request,user_name):
     user = User.objects.create_user(user_name, 'lennon@thebeatles.com', user_name)
     if user:
         return render_to_response('signup.html',{'status':user})

@csrf_exempt
def authenticate_user(request):  
    data= json.loads(request.body)
    user_name = data.get('user_name')
    passw=data.get('passw')
    user = authenticate(username=user_name, password=passw)
    if user is not None:
    # the password verified for the user
        if user.is_active:
            uid=user.id
            request.session['u_id'] = uid
            return HttpResponse(uid)
    else:
    # the authentication system was unable to verify the username and password
        return("in-valid")   
def new_task(request,user_id):
    #u_id=request.session['u_id']
    #print u_id
    return render_to_response('createtask.html',{'u_id':user_id})     