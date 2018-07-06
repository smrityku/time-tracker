from django.contrib import admin
from .models import Attendence
from .models import Leave
from .models import LeaveTracker


admin.site.register(Attendence)
admin.site.register(Leave)
admin.site.register(LeaveTracker)