# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
import models

# Create your views here.
def index(request):
    if 'user' in request.session:
        return redirect('/dashboard')
    else:
        return render(request, 'playerapp/index.html')

def login(request):
    if request.method == 'POST':
        valid, result = User.objects.valid_login(request.POST)
        if result[0]:
            request.session['user'] = result
            return redirect('/dashboard')
        else:
            for error in result:
                messages.error(request, error)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        valid, result = models.User.objects.valid_register(request.POST)
        if valid:
            request.session['user'] = result.id
            return redirect('/dashboard')
        else:
            for error in result:
                messages.error(request, error)
    return redirect('/')

def dashboard(request):
    if not 'user' in request.session:
        return redirect('/')
    return render(request, 'playerapp/dashboard.html')

def logout(request):
    
