from django.contrib import admin
from .models import Attendence
from .models import Leave
from .models import LeaveTracker


class AttendenceAdmin(admin.ModelAdmin):
	list_display = ('user', 'check_in_date', 'in_time', 'out_time')

admin.site.register(Attendence, AttendenceAdmin)
admin.site.register(Leave)
admin.site.register(LeaveTracker)