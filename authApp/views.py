from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method=='POST':
        form=forms.RegistationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Accounnt created successfully')
            return redirect('register')
    else:
        form=forms.RegistationForm()
    return render(request,'register.html',{'form':form,'type':'Sign '})

def userlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('profile')
            else:
                messages.warning(request, 'Login information is incorrect')
                return redirect('userlogin')
        else:
            messages.error(request, 'Invalid login credentials')
            return render(request, 'login.html', {'form': form, 'type': 'Login'})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form, 'type': 'Login'})
    
def profile(request):
    return render(request,'profile.html')

@login_required
def profileUpdate(request):
    if request.method=="POST":
        form=forms.changeuserdata (request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Updated successfully')
            return redirect('profile')
    else:
        form=forms.changeuserdata(instance=request.user)
    return render(request,'Update_profile.html',{'form':form,})

def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change.html', {'form' : form})


def user_logout(request):
    logout(request)
    messages.success(request, 'LogOut Successfully')
    return redirect('userlogin')

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Updated Successfully')
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'change2.html', {'form': form})
    else:
        return redirect('login')