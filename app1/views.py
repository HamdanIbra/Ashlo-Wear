from django.shortcuts import render, redirect
from . models import *
import bcrypt
from django.contrib import messages


# def index(request):
#     # mainnnn pagee
#     return render(request, "index.html")

def log(request):
    return render(request, "login.html")


def login(request):
    errors = User.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email).first()
    if user:
        if bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/success')
    messages.error(request, 'Invalid Credentials')
    return redirect('/')


def register(request):
    return render(request, "register.html")


def registration(request):
    errors = User.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=fname, last_name=lname,
                            email=email, password=hashed)
        user = User.objects.last()
        request.session['user_id'] = user.id
    return redirect('/success')
