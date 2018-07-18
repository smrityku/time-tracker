import datetime
from dateutil.relativedelta import relativedelta

from .models import Attendance

def get_monthly_summary(user):
	iterate = 0
	entry_time = 0
	total_hours = 0
	average_hours = 0
	user_attendence_this_month = Attendance.objects.filter(check_in_date__year=datetime.date.today().year,
														   check_in_date__month=datetime.date.today().month,
														   user=user)

	for attendence in user_attendence_this_month:
		entry_time = entry_time + times_in_seconds(attendence.in_time)
		if attendence.out_time is not None:
			total_hours = total_hours + diff_times_in_seconds(attendence.in_time, attendence.out_time)
			iterate += 1

	num = len(user_attendence_this_month)
	if num != 0:
		entry_time = entry_time / num
		entry_time = datetime.datetime.utcfromtimestamp(entry_time).strftime("%I:%M %p")
	if iterate != 0:
		average_hours = str(datetime.timedelta(seconds=(int(total_hours / iterate))))
		total_hours = str(datetime.timedelta(seconds=total_hours))

	return [user, entry_time, average_hours, total_hours]

def get_current_prev_month_summary(user):
	iterate = 0
	current_entry_time = 0
	current_total_hours = 0
	current_average_hours = 0
	prev_entry_time = 0
	prev_total_hours = 0
	prev_average_hours = 0
	prev_year = (datetime.date.today() - relativedelta(months=1)).year
	prev_month = (datetime.date.today() - relativedelta(months=1)).month
	user_attendence_this_month = Attendance.objects.filter(check_in_date__year=datetime.date.today().year,
														   check_in_date__month=datetime.date.today().month,
														   user=user)
	user_attendance_prev_month = Attendance.objects.filter(check_in_date__year=prev_year,
														   check_in_date__month=prev_month,
														   user=user)

	for attendance in user_attendence_this_month:
		current_entry_time = current_entry_time + times_in_seconds(attendance.in_time)
		if attendance.out_time is not None:
			current_total_hours = current_total_hours + diff_times_in_seconds(attendance.in_time, attendance.out_time)
			iterate += 1

	num = len(user_attendence_this_month)
	if num != 0:
		current_entry_time = current_entry_time / num
		current_entry_time = datetime.datetime.utcfromtimestamp(current_entry_time).strftime("%I:%M %p")
	if iterate != 0:
		current_average_hours = str(datetime.timedelta(seconds=(int(current_total_hours / iterate))))
		current_total_hours = str(datetime.timedelta(seconds=current_total_hours))

	iterate = 0
	for attendance in user_attendance_prev_month:
		prev_entry_time = prev_entry_time + times_in_seconds(attendance.in_time)
		if attendance.out_time is not None:
			prev_total_hours = prev_total_hours + diff_times_in_seconds(attendance.in_time,
																			  attendance.out_time)
			iterate += 1

	num = len(user_attendance_prev_month)
	if num != 0:
		prev_entry_time = prev_entry_time / num
		prev_entry_time = datetime.datetime.utcfromtimestamp(prev_entry_time).strftime("%I:%M %p")
	if iterate != 0:
		prev_average_hours = str(datetime.timedelta(seconds=(int(prev_total_hours / iterate))))
		prev_total_hours = str(datetime.timedelta(seconds=prev_total_hours))

	return [user, current_entry_time, current_average_hours, current_total_hours,
			prev_entry_time, prev_average_hours, prev_total_hours]

def get_daily_total(time_now, in_time):
	total_hours = 0
	total_hours = diff_times_in_seconds(in_time, time_now)
	return str(datetime.timedelta(seconds=total_hours))

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