from django.contrib.auth import login
from django.shortcuts import render, redirect
from app2.forms import CombinedRegistrationForm
from django.contrib.auth.models import User
from app2.models import newuser


def signup_view(request):
    if request.method == 'POST':
        form = CombinedRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = CombinedRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})
