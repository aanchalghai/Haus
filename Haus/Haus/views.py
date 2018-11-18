from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from .forms import UserRegistrationForm
from users.forms import NameForm,PersonalInfoForm,RentListingsForm,PgListingsForm,SellListingsForm
from django.urls import reverse
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth import login as ulogin
from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView
from django.db import transaction
from django.contrib.auth import get_user_model
from users.models import RentListings,PgListings,SellListings



class Index(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Agents(TemplateView):
    template_name = 'agents.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class Detail(TemplateView):
    template_name = 'details.html'

@login_required
@transaction.atomic
def listings_rent(request):
    user = request.user
    if request.method == 'POST':
        listing_form = RentListingsForm(request.POST,request.FILES)
        if listing_form.is_valid():
            listing = listing_form.save(commit=False)
            listing.user = request.user
            # if 'pictures' in request.FILES:
            #     listing.pictures = request.FILES['pictures']
            listing.save()
            messages.success(request,('Your listing has been successfully created!'))
            return HttpResponseRedirect(reverse('listing_rent'))
        else:
            messages.error(request,(listing_form.errors))
    else:
        listing_form = RentListingsForm()
    return render(request, 'listing_rent.html',
                          {'listing_form': listing_form,})

@login_required
@transaction.atomic
def listings_pg(request):
    user = request.user
    if request.method == 'POST':
        listing_form = PgListingsForm(request.POST,request.FILES)
        if listing_form.is_valid():
            listing = listing_form.save(commit=False)
            listing.user = request.user
            # if 'pictures' in request.FILES:
            #     listing.pictures = request.FILES['pictures']
            listing.save()
            messages.success(request,('Your listing has been successfully created!'))
            return HttpResponseRedirect(reverse('listing_pg'))
        else:
            messages.error(request,(listing_form.errors))
    else:
        listing_form = PgListingsForm()
    return render(request, 'listing_pg.html',
                          {'listing_form': listing_form,})

@login_required
@transaction.atomic
def listings_selling(request):
    user = request.user
    if request.method == 'POST':
        listing_form = SellListingsForm(request.POST,request.FILES)
        if listing_form.is_valid():
            listing = listing_form.save(commit=False)
            listing.user = request.user
            # if 'pictures' in request.FILES:
            #     listing.pictures = request.FILES['pictures']
            listing.save()
            messages.success(request,('Your listing has been successfully created!'))
            return HttpResponseRedirect(reverse('listing_selling'))
        else:
            messages.error(request,(listing_form.errors))
    else:
        listing_form = SellListingsForm()
    return render(request, 'listing_selling.html',
                          {'listing_form': listing_form,})

def properties(request):
    data1 = RentListings.objects.all()
    data2 = PgListings.objects.all()
    data3 = SellListings.objects.all()
    if request.method == 'POST':
        messages.success(request,('Your enquiry has been sent sucessfully!, our support team will contact you shortly.'))
    return render(request, 'properties.html',{'data1':data1,'data2':data2,'data3':data3,})

@login_required
@transaction.atomic
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        name_form = NameForm(request.POST, instance=request.user)
        personal_form = PersonalInfoForm(request.POST, instance=request.user.personalinfo)
        if name_form.is_valid() and personal_form.is_valid():
            name_form.save()
            personal_form.save()
            messages.success(request,('Your profile was successfully updated!'))
            return HttpResponseRedirect(reverse('form'))
        else:
            messages.error(request,(name_form.errors,personal_form.errors))
    else:
        name_form = NameForm(instance=request.user)
        personal_form = PersonalInfoForm(instance=request.user.personalinfo)
    return render(request, 'form.html',
                          {'name_form': name_form,
                           'personal_form': personal_form,})

def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        if user_form.is_valid() and user_form.cleaned_data['password1'] == user_form.cleaned_data['password2']:
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            messages.success(request,('Registration complete'))
            return HttpResponseRedirect(reverse('signup'))
        elif user_form.data['password1'] != user_form.data['password2']:
            messages.error(request,('Passwords do not match'))
        else:
            messages.error(request,user_form.errors)
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        else:
            user_form = UserRegistrationForm()
    return render(request,'signup.html',
                         {'user_form':user_form,})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                ulogin(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request,"Your account is not active")
                return render(request,'login.html')
        else:
            messages.error(request,"Invalid Username or Password")
            return render(request,'login.html')
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'login.html')

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))
