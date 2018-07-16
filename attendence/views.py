from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django import template
import datetime
import time
from datetime import date

from .models import Attendance
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def home(request):		
	if request.user.is_authenticated:
		now = datetime.datetime.now()
		today10am = now.replace(hour=10, minute=0, second=0, microsecond=0)
		user_info = []
		try:
			user_attendence = Attendance.objects.filter(check_in_date=datetime.datetime.now(), user=request.user)
		except:		
			user_Attendance = {}

		entry_time = 0
		total_hours = 0
		average_hours = 0
		iterate = 0

		if request.method == 'POST':
			if request.POST['type'] == '1':
				if not user_attendence:
					Attendance.objects.create(user=request.user, check_in_date=datetime.datetime.now(),
						in_time=datetime.datetime.now().time(), created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
			elif request.POST['type'] == '2':
				user_attendence.update(out_time = datetime.datetime.now().time())

		user_attendence_this_month = Attendance.objects.filter(check_in_date__year=datetime.date.today().year, check_in_date__month=datetime.date.today().month, user=request.user)

		for attendence in user_attendence_this_month:
			entry_time = entry_time + times_in_seconds(attendence.in_time)
			if attendence.out_time is not None:
				total_hours = total_hours + diff_times_in_seconds(attendence.in_time, attendence.out_time)
				iterate += 1

		num = len(user_attendence_this_month)
		if num != 0:
			entry_time = entry_time/num
			entry_time = datetime.datetime.utcfromtimestamp(entry_time).strftime("%I:%M %p")
		if iterate != 0:
			average_hours = str(datetime.timedelta(seconds=(int(total_hours/iterate))))
			total_hours = str(datetime.timedelta(seconds=total_hours))

		user_info = [entry_time, average_hours, total_hours]

		try:
			attendences = Attendance.objects.filter(check_in_date=datetime.datetime.now())
		except:
			attendences = {}
		
		return render(request, 'home.html', 
			{'attendences': attendences, 'user_attendence': user_attendence.first, 'today10am': today10am, 
				'user_length': len(attendences), 'date_today': datetime.datetime.now().strftime("%d %B, %Y"),
				'user_info': user_info})
	else:
		return redirect('login')

def attendance(request):
	attendances = Attendance.objects.all()

	return render(request, 'attendance.html', {'attendences': attendances})

def leave_tracker(request, pk):
	attendances = Attendance.objects.get(pk=pk)

	return render(request, 'home.html', {'attendances': attendances})

def diff_times_in_seconds(t1, t2):
	h1, m1, s1 = t1.hour, t1.minute, t1.second
	h2, m2, s2 = t2.hour, t2.minute, t2.second
	t1_secs = s1 + 60 * (m1 + 60*h1)
	t2_secs = s2 + 60 * (m2 + 60*h2)
	return abs(t2_secs - t1_secs)

def times_in_seconds(t1):
	h1, m1, s1 = t1.hour, t1.minute, t1.second
	t1_secs = s1 + 60 * (m1 + 60*h1)
	return t1_secs
