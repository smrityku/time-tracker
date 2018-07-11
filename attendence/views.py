from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django import template
import datetime
import time
from django.contrib.auth.models import User

from .models import Attendence
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def home(request):	
	now = datetime.datetime.now()
	today10am = now.replace(hour=10, minute=0, second=0, microsecond=0)
	try:
		user_attendence = Attendence.objects.filter(check_in_date=datetime.datetime.now(), user=request.user)
	except:		
		user_attendence = {}

	if request.method == 'POST':
		if request.POST['type'] == '1':
			if not user_attendence:
				Attendence.objects.create(user=request.user, check_in_date=datetime.datetime.now(), 
					in_time=datetime.datetime.now().time(), created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
		elif request.POST['type'] == '2':
			user_attendence.update(out_time = datetime.datetime.now().time())
	try:
		attendences = Attendence.objects.filter(check_in_date=datetime.datetime.now())
	except:
		attendences = {}

	if request.user.is_authenticated:
		return render(request, 'home.html', 
			{'attendences': attendences, 'user_attendence': user_attendence.first, 'today10am': today10am, 
				'user_length': len(attendences), 'date_today': datetime.datetime.now().strftime("%d %B, %Y")})
	else:
		return redirect('login')

def attendence(request):
	attendences = Attendence.objects.all()

	return render(request, 'attendence.html', {'attendences': attendences})

def leave_tracker(request, pk):
	attendences = Attendence.objects.get(pk=pk)

	return render(request, 'home.html', {'attendences': attendences})
