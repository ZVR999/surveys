# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'survey_app/index.html') 

def result(request):
    return render(request,'survey_app/result.html')

def process(request):
    # Gather all form data and place into a session key
    request.session['your_name'] = request.POST['your_name']
    request.session['dojo_location'] = request.POST['dojo_location']
    request.session['favorite_language'] = request.POST['favorite_language']
    request.session['comment'] = request.POST['comment']

    # Creates a counter with initial submit of a survey
    if not 'counter' in request.session:
        request.session['counter'] = 1
        return redirect('/result')
    # Add one to the counter with every submission 
    request.session['counter'] += 1
    return redirect('/result')

def reset(request):
    request.session['counter'] = 0
    return redirect('/result')

