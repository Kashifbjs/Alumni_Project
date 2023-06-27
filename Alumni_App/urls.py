from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name = 'Login'),
    path('Dashboard', views.Dashboard, name = 'Dashboard'),
    path('Logout', views.Logout, name = 'Logout'),
    path('Register', views.Register, name = 'Register'),
    path('Profile', views.Profile, name = 'Profile'),
    path('Contact', views.Contact, name = 'Contact'),
]