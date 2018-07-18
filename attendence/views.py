from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .utils import *
import datetime

from .models import Attendance

def home(request):		
	if request.user.is_authenticated:
		now = datetime.datetime.now()
		today10am = now.replace(hour=10, minute=0, second=0, microsecond=0)
		user_info = []
		try:
			user_attendence = Attendance.objects.filter(check_in_date=datetime.datetime.now(), user=request.user)
		except:		
			user_Attendance = {}

		status = False
		if request.method == 'POST':
			if request.POST['type'] == '1':
				if not user_attendence:
					if datetime.datetime.now().time() <= today10am.time():
						status = True
					Attendance.objects.create(user=request.user, check_in_date=datetime.datetime.now(),
						in_time=datetime.datetime.now().time(), status=status, created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
			elif request.POST['type'] == '2':
				in_time = user_attendence[0].in_time
				user_attendence.update(out_time = datetime.datetime.now().time())
				out_time = user_attendence[0].out_time
				total_hours = diff_times_in_seconds(out_time, in_time)
				user_attendence.update(total_hours = str(datetime.timedelta(seconds=total_hours)))

		user_info = get_monthly_summary(request.user)

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
	current_arr = []
	if 'search' in request.GET and request.GET['search']:
		query = request.GET['search']
		users = User.objects.filter(username__icontains=query)
	else:
		users = User.objects.all()

	for user in users:
		current_arr.append(get_current_prev_month_summary(user))

	return render(request, 'attendance.html', {'current_arr': current_arr})

def user_attendance(request, pk):
	user = User.objects.get(pk=pk)

	user_attendence_this_month = Attendance.objects.filter(check_in_date__year=datetime.date.today().year,
														   check_in_date__month=datetime.date.today().month,
														   user=user)
	return render(request, 'user_attendance.html', {'attendances': user_attendence_this_month,
													'user': user,
													'check_in_date_year': datetime.date.today().year,
													'check_in_date_month': datetime.date.today().strftime("%B")})


def salaat_time(request):
	return render(request, 'salaat_time.html')

def leave_tracker(request, pk):
	attendances = Attendance.objects.get(pk=pk)

	return render(request, 'home.html', {'attendances': attendances})
