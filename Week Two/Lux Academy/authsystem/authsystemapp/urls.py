from django.urls import path

from . import views

urlpatterns = [
    # get urls
    path('', views.login, name='login'),
    path('dashboard', views.index, name='dashboard'),
    path('registration', views.registration, name='registration'),
    path('register', views.register, name='register')
]