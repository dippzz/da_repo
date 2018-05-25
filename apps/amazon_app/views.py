# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    response = "Hello, this is my first project"
    return render(request, "amazon_app/index.html")

def registerSubmit(request):
   if request.method == "POST":
       print request.POST
       result = User.objects.validate_registration(request.POST)
       if type(result) == list:
            for x in result:
               messages.error(request, x)
               return redirect('/')
       else:
            request.session['id'] = result.id
            request.session['name'] = request.POST['name']
        #    request.session['role'] = request.POST['role']
            messages.success(request, 'You have registered successfully!')
            return render(request, "amazon_app/dashboard.html")
        #    return redirect('/eduPortal/registerPage')


def loginUser(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for x in result:
            messages.error(request, x)
        return redirect('/')
    else:       
        request.session['id'] = result.id
        request.session['name'] = result.name
        # request.session['role'] = result.role
        print 'login success'#, request.session['role'], result.role
        messages.success(request, 'You have logged in!')
        # if not result.level:
        return render(request, "amazon_app/dashboard.html")
        # else:
            # return redirect('/eduPortal/dashboardTwo')