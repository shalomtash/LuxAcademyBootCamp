from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse


# import pdb; pdb.set_trace()
from authsystemapp.forms import RegisterForm


def index(request):
    return render(request, "authsystemapp/index.html")


def login(request):
    return render(request, 'authsystemapp/login.html')


def registration(request):
    return render(request, "authsystemapp/registration.html")


def register(request):
    # if request.method == 'POST':
        form = RegisterForm(request.POST)
    # print("########## "+request.POST)
        if form.is_valid():
            uname = request.GET['username']
            mail = request.GET['email']
            pword = request.GET['password']
            user = User.objects.create(username=uname, email=mail, password=pword)
            # breakpoint(user)
            user.save()
            messages.success(request, 'Data has been submitted')
            return render(request, 'authsystemapp/registration.html',{'form': form})
