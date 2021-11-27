from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # display blank form
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # log the user in 
            login(request, new_user)
            # and then redirect to home page.
            return redirect('app_renekton:index')

    # if the form is blank or invalid
    context = {'form': form}
    return render(request, 'registration/register.html', context)
