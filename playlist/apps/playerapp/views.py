# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'playerapp/index.html')

def login(request):
    if 'user' in session:
        return redirect('/dashboard')
    else:
        return redirect('/')

def register(request):
    print request.POST
    if 'user' in session:
        return redirect('/dashboard')
    else:
        return redirect('/')
