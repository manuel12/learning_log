""" Defines URL patterns for learning_logs."""

from django.urls import path

from django.contrib.auth.views import LoginView

from .views import logout_view, register


app_name = 'users'

urlpatterns = [
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', logout_view, name='logout'),
	path('register/', register, name='register')
]