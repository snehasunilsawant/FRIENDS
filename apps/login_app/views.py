# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import User

from django.contrib import messages
# Create your views here.
def index(request):
    
    return render(request,'login_app/index.html')

def register(request):    
    results = User.objects.validate(request.POST)
    print results
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        print "user is created"
        messages.success(request,"User created sucessfully. Please login with Email id and password")
    else:
        for i in results['errors']:
            messages.error(request,i)
    return redirect('/main/')

def login(request):
    print request.POST
    results = User.objects.loginvalidation(request.POST)
    if results['status'] == False :
        messages.error(request,"Please enter correct Email id and password. Try Again !!!")
        return redirect('/main/')
    request.session['email'] = results['user'].email
    request.session['name'] = results['user'].name
    request.session['userid'] = results['user'].id
    return redirect('/friends/')


def logout(request):
    request.session.flush()
    return redirect('/main/')