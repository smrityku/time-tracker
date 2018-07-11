from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
import datetime
from django.contrib.auth.models import User

from .views import home
from .models import Attendence, Leave, LeaveTracker

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

class AttendenceTests(TestCase):
    def setUp(self):
    	user = User.objects.create_user(username='testuser', password='12345')
    	Attendence.objects.create(user=user, check_in_date=datetime.datetime.now(), in_time=datetime.datetime.now().time())

    def test_attendence_view_success_status_code(self):
    	url = reverse('attendence')
    	response = self.client.get(url)
    	self.assertEquals(response.status_code, 200)
