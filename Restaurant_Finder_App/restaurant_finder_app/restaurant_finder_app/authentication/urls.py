# authenticatiom/urls.py
from django.conf.urls import url
from authentication import views

urlpatterns = [
     url(r'^$', views.LoginPageView.as_view()),
]