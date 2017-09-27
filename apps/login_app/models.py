# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# import date
# import datetime

import re

import bcrypt

print bcrypt

# Create your models here.
class UserManager(models.Manager):  
        
    def loginvalidation(self,postData):
        results = { 'status' : True,'errors' : [] , 'user' : None}
        users = self.filter(email = postData['email'])

        if len(users) < 1:
            results['status'] = False
        else :
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = False
        return results   
        
    def creator(self,postData):
        encryptedPassword = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

        user = self.create(name=postData['name'], alias=postData['alias'], email=postData['email'], password=encryptedPassword, dob=postData['date'])

        return user

    def validate( self, postData ):
        print postData

        results = { 'status' : True,'errors' : [] }

        if len( postData['name'].strip() ) < 3:
            results['errors'].append("Name field must be at least 3 characterst")
            results['status'] = False

        if len(postData['alias'].strip()) < 3:
            results['errors'].append("Alias field must be at least 3 characters")
            results['status'] = False

        if not re.match("[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]", postData['email']):
            results['errors'].append("Given Email is invalid")
            results['status'] = False
        
        if postData['password'] != postData['c_password'] :
            results['errors'].append("Given Passwords do not match")
            results['status'] = False

        if len(postData['password']) < 8 :
            results['errors'].append("Password must be at least 8 characters")
            results['status'] = False

        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append("Given Email id already exist ")
            results['status'] = False

        return results


class User(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    friends_with = models.ManyToManyField( "self" , null=True, blank=True, related_name ="my_friends") 
    objects = UserManager()
 