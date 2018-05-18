from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#start views here

#Home
@login_required
def home(request):
    numbers = [1,2,3,4,5]
    name = "John Doe"
    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)


#Register
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/reg_form.html', {'form' : form})

#View Profile
@login_required
def view_profile(request):
    if request.user.is_client:
        args = {'user':request.user}
        return render(request, 'accounts/profile.html', args)
    elif request.user.is_admin:
        return HttpResponse('<h1>Page not found</h1>')
    else:
        args = {'user': request.user}
        return render(request, 'accounts/profile.html', args)

#Edit Profile
@login_required
def edit_profile(request):
    if request.user.is_client:
        return HttpResponse('<h1>Page not found</h1>')
    elif request.user.is_admin:
        return HttpResponse('<h1>Page not found</h1>')
    else:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('/accounts/profile')
        else:
            form = EditProfileForm(instance=request.user)
        return render(request, 'accounts/edit_profile.html', {'form' : form})

#Change Password
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user=form.user)
            return redirect('/accounts/profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {'form' : form})



