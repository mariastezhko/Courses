from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# Create your views here.

from models import *

def index(request):
    if request=='POST':
        return redirect('/')
    else:
        return render(request, 'courses_app/index.html', {"courses": Course.objects.all()})

def create(request):
    print("************")
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    else:
        name = request.POST['name']
        desc = request.POST['desc']
        Course.objects.create(name = name, desc = desc)
        return redirect('/')

def delete_form(request, number):
    return render(request, 'courses_app/delete.html', {"course": Course.objects.get(id=number)})

def delete(request, number):
    Course.objects.get(id=number).delete()
    return redirect('/')
