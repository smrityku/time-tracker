from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import template

from .models import Attendence


def home(request):
	attendences = Attendence.objects.all()
	if request.user.is_authenticated:
		return render(request, 'home.html', {'attendences': attendences})
	else:
		return redirect('login')

def attendence(request):
	attendences = Attendence.objects.all()

	return render(request, 'attendence.html', {'attendences': attendences})

def leave_tracker(request, pk):
	attendences = Attendence.objects.get(pk=pk)

	return render(request, 'home.html', {'attendences': attendences})


