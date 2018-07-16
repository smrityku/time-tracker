from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()

	return render(request, 'signup.html', {'form': form})
