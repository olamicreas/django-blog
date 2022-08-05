from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            username = form.data.get('username')
            messages.success(request, f'Account created successfully for {username}' )
            return redirect('login')
       

    return render(request, 'user/register.html', {'form': form})

def profile(request):
    return render(request, 'user/profile.html')