from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm, NewUserForm
from .models import ContactDetails
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def firstpage(request):
    return render(request , 'base/firstpage.html')

def home(request):
    details = ContactDetails.objects.all()
    context = {'details': details}
    return render(request , 'base/home.html', context)

@login_required(login_url='/login')
def table(request):
    user=request.user
    details = ContactDetails.objects.filter(added_by=user)
    headers = ['First-name', 'Last-name', 'Gender','Age','Address','Phone','Religion','nation']
    context = {'details': details, 'headers':headers}
    return render(request , 'base/table.html', context)

@login_required(login_url='/login')
def add(request):
    form = ContactForm()
    user=request.user
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            added_by=request.user
            f=form.save(commit=False)
            f.added_by=added_by
            f.save()

            return redirect('table') 
        else:
            form = ContactForm()
    return render(request, 'base/add.html', {'form': form})

@login_required(login_url='/login')
def contactProfile(request,pk):
    contact = ContactDetails.objects.get(id=pk)
    context = {'contact' : contact}
    return render(request, 'base/contactprofile.html', context)

@login_required(login_url='/login')
def deleteContact(request, pk):
    contact = ContactDetails.objects.get(id=pk)
    context = {'contact' : contact}

    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    return render(request, 'base/delete.html', context ) 

@login_required(login_url='/login')
def allcontacts(request):
    user=request.user
    details = ContactDetails.objects.filter(added_by=user)
    context = {'details': details}
    return render(request , 'base/allcontacts.html', context)

@login_required(login_url='/login')
def updateContact(request,pk):
    contact = ContactDetails.objects.get(id=pk)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        contact.fname = request.POST.get('fname')
        contact.lname = request.POST.get('lname')
        contact.gender = request.POST.get('gender')
        contact.age = request.POST.get('age')
        contact.address = request.POST.get('address')
        contact.phone = request.POST.get('phone')
        contact.religion = request.POST.get('religion')
        contact.nation = request.POST.get('nation')
        contact.save()
        
        return redirect('home')

    context = {'form': form, 'contact': contact}
    return render(request, 'base/add.html', context)

def registerUser(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request , "Registered Successfully")
            return redirect('home')
        messages.error(request, "There was an error during registration")
    form = NewUserForm()
    context = {"form" : form}
    return render (request, 'base/register.html', context)

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in.")
                return redirect("home")
            else:
                messages.error(request, "Username or Password is Incorrect.")
        else:
            messages.error(request, "Username or Password is Incorrect.")
    form = AuthenticationForm()
    context = {"form" : form}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, "Successfully logged out")
    return redirect('firstpage')