from django.db import models
from django.contrib.auth.models import User

class Attendance(models.Model):
    check_in_date = models.DateField(auto_now_add=True)
    in_time = models.TimeField(null=True)
    out_time = models.TimeField(null=True)
    user = models.ForeignKey(User, related_name='attendences', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
    	return self.user.username

class Leave(models.Model):
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    leave_type = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    duration = models.IntegerField(default=1)
    user = models.ForeignKey(User, related_name='leaves', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
    	return self.user.username

class LeaveTracker(models.Model):
	accured_casual = models.IntegerField(default=0)
	accured_medical = models.IntegerField(default=0)
	carry_forwarded_casual = models.IntegerField(default=0)
	carry_forwarded_medical = models.IntegerField(default=0)
	consumed_casual = models.IntegerField(default=0)
	consumed_medical = models.IntegerField(default=0)
	user = models.ForeignKey(User, related_name='leave_trackers', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)

	def __str__(self):
		return self.user.username
