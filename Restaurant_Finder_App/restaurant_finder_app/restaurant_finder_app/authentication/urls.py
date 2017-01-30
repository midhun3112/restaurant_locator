# authenticatiom/urls.py

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from authentication.utils import views
from authentication.utils.forms import LoginForm

urlpatterns = [
	 url(r'^logout/$', views.logout_page),
     # url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
     url(r'^register/$', views.register, name="register"),
     url(r'^register/success/$', views.register_success),
     url(r'^login/$',auth_views.login, {'template_name': 'login_page.html', 'authentication_form': LoginForm}, name="login"), 
     url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
     url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
     url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
     url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
      auth_views.password_reset_confirm, name='password_reset_confirm'),
     url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]