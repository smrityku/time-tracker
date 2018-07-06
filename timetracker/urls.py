from django.conf.urls import include, url

from django.contrib import admin

from attendence import views

from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = [
	url(r'^$', views.home, name='home'),

    url(r'^admin/', admin.site.urls),
]
