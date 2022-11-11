from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def register(request):
    form = CreateUserForm()
    print(request.method)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('/authentication/loginUser')
        else:
            # get all the errors returned by the form
            errors = form.errors.as_data()
            # loop through the errors and add them to the messages
            for error in errors:
                messages.error(request, errors[error][0])
            return redirect('/authentication/register')
    context = {'form': form}
    return render(request, 'authenticate/register.html', context)


@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, 'You have successfully logged in')
            # return to the page the user was on before login
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('/authentication/loginUser')
    context = {}
    return render(request, 'authenticate/login.html', context)
