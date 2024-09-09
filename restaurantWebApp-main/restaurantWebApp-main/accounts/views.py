from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import PhoneNumber
from django.contrib import messages
from django.contrib.auth import login as login_user, authenticate, logout as logout_user
import json

# Create your views here.
def login(request):
    if request.method == 'POST':
        body = request.POST

        username = body.get('username')
        password = body.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_user(request, user)
            return redirect('/')    
        else: 
            messages.error(request, "Wrong Credentials. Check Again.")
            return render(request,'login.html')
    else:
        return render(request, 'login.html')
    

def logout(request):
    logout_user(request)
    return redirect('/')
    

def signup(request):
    if request.method == 'POST':
        body = request.POST

        username = body.get('username')
        email = body.get('email')
        phone = body.get('phone')
        password = body.get('password')
        password2 = body.get('password2')

        if(len(phone)) < 10 or len(phone) > 10:
            print(phone)
            messages.error(request, "Your phone number field entered is not correct, make sure its exactly 10 digits.")
            return render(request , 'reservation.html')
        
        if password == password2:
            user = User.objects.create_user(username, email, password)
            user.save()
            if phone is not None:
                PhoneNumber.objects.create(user=user, number=phone)
        else: 
            messages.error(request, "Passwords do not match.")
            return render(request,'signup.html')

        return redirect('accounts:login_user')
    else:
        return render(request, 'signup.html')
    

def me(request):
    try:
        phone = PhoneNumber.objects.get(user__id=request.user.id)
    except:
        phone = None

    context = {
        'phone': phone
    }

    return render(request, 'account.html', context)


def edit_account(request):
    if request.method == 'POST':
        body = request.POST
        to_save = True

        phone = body.get('phone')
        email = body.get('email')

        try:
            _phone = PhoneNumber.objects.get(number=phone)
            messages.error('Phone number already in use.')
            to_save = False
        except:
            pass

        try:
            _email = User.objects.get(email=email)
            messages.error('Email already in use.')
            to_save = False
        except:
            pass

        if to_save:
            user = User.objects.get(id=request.user.id)
            user.email = email
            user.save()

            try: 
                number = PhoneNumber.objects.get(user__id=user.id)
                number.number = phone
                number.save()
            except:
                PhoneNumber.objects.create(user=user, number=phone)

            return redirect('accounts:me')
            
    try:
        phone = PhoneNumber.objects.get(user__id=request.user.id)
    except:
        phone = None

    context = {
        'phone': phone
    }

    return render(request, 'edit_account.html', context)


def change_password(request):
    if request.method == 'POST':
        body = request.POST
        user = request.user

        old_password = body.get('old_password')
        new_password = body.get('new_password')
        new_password2 = body.get('new_password2')

        if user.check_password(old_password):
            if new_password == new_password2:
                user.set_password(new_password)
                messages.success(request, 'Password changed successfully.')
                return redirect('accounts:me')
            else:
                messages.error(request, 'New passwords do not match.')
        else:
            messages.error(request, 'Your current password is incorrect.')
        
    return render(request, 'change_password.html')