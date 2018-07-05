from django.shortcuts import render
from django.http import HttpResponse
from django import template

from .models import Attendence


def home(request):
	attendences = Attendence.objects.all()

	return render(request, 'home.html', {'attendences': attendences})
