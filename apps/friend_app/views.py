# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , redirect

from ..login_app.models import User

# from models import Friend

# Create your views here.
def index(request):
    if 'email' not in request.session:
        return redirect('/main/')
    user = User.objects.get(id=request.session['userid'])
    myList = []
    myList.append(request.session['userid'])
    for i in user.friends_with.all():
        myList.append(i.id)
    context = {
        'count' : User.objects.all().count(),
        'user' : user,
        'otherUsers' : User.objects.exclude(id__in=myList),
           }
    return render(request,'friend_app/index.html',context)


def add(request,friendid):
    if 'email' not in request.session:
        return redirect('/main/')
    friend = User.objects.get(id=friendid)
    user = User.objects.get(id=request.session['userid'])  
    user.friends_with.add(friend)      
    return redirect('/friends/')

def remove(request,friendid):
    if 'email' not in request.session:
        return redirect('/main/')
    user = User.objects.get(id=request.session['userid'])
    friend = User.objects.get(id=friendid)
    user.friends_with.remove(friendid)
    return redirect('/friends/')


def show(request,userid):
    if 'email' not in request.session:
        return redirect('/main/')
    context = {
        'user': User.objects.get(id=userid),
    }
    return render(request,'friend_app/show.html',context)