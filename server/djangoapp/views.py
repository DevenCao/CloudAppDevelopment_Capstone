from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    return render(request, 'djangoapp/about.html')


# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, 'djangoapp/contact.html')


# Create a `login_request` view to handle sign in request
def login(request):
    print('----------login---------', request.method)
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
        else:
            messages.info(request, 'Credential Invalid')    

        return redirect('djangoapp:index')   
    else:
        return render(request, 'djangoapp/index.html')


# Create a `logout_request` view to handle sign out request
def logout(request):
    auth.logout(request)
    return redirect('djangoapp:login')


# Create a `registration_request` view to handle sign up request
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already used, please use another one')
            return redirect('djangoapp:registration')
        else:
            user = User.objects.create(username=username, first_name=firstname, last_name=lastname, password=password)
            user.save
            return redirect('djangoapp:login')
    else:
        return render(request, 'djangoapp/registration.html')


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/index.html', context)
    else:
        return redirect('djangoapp:login')


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...
