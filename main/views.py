from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.defaults import page_not_found
from .models import *
from bs4 import BeautifulSoup
import requests
import json
import urllib
import ast
from Crypto.Cipher import AES
import binascii
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # passphrase = request.POST.get('passphrase')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                # return render(request, 'main/home.html')
                return redirect("main:home")
        else:
            return render(request, 'main/login.html', {'error_message': 'Invalid login'})
    else:
        if request.user.is_authenticated is True:
            return render(request, 'main/home.html')
        elif request.GET.get('next'):
            return render(request, 'main/login.html', {'error_message': 'You must log in to see this page' })
    return render(request, 'main/login.html')
    
def logout_user(request):
    logout(request)
    # return render(request, 'main/home.html')
    return redirect("main:home")

def home(request):
    return render(request, 'main/home.html')

def userInfo(request):
    return render(request, 'main/userInfo.html')

def technicianList(request):
    
    x={}
    x['technicianList'] = User.objects.filter(groups__name="Technicians")
    return render(request, 'main/technicianList.html', x)
    
def requestList(request):
    
    x={}
    x['requestList'] = RequestEntry.objects.all()
    
    return render(request, 'main/requestList.html', x)
# Create your views here.
