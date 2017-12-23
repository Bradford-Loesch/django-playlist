# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import models

# Create your views here.
def index(request):
    return render(request, 'playerapp/index.html')

def login(request):
    result = User.objects.valid_login(request.POST)
    if 'user' in request.session:
        return redirect('/dashboard')
    else:
        return redirect('/')

def register(request):
    print request.POST['bday']
    result = Users.objects.valid_register(request.POST)
    print result
    if result[0]:
        return redirect('/dashboard')
    else:
        return redirect('/')
