from django.contrib import admin
from .models import Attendance
from .models import Leave
from .models import LeaveTracker


class AttendanceAdmin(admin.ModelAdmin):
	list_display = ('user', 'check_in_date', 'in_time', 'out_time')

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Leave)
admin.site.register(LeaveTracker)