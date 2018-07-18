from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from attendence import views
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^signup/$', accounts_views.signup, name='signup'),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
	url(r'^attendances/', views.attendance, name='attendance'),
    url(r'^attendance/(?P<pk>\d+)/$', views.user_attendance, name='user_attendance'),
	url(r'^salaat_times/', views.salaat_time, name='salaat_time'),
	url(r'^leave_tracker/(?P<pk>\d+)/$', views.leave_tracker, name='leave_tracker'),
	url(r'^admin/', admin.site.urls),
]
