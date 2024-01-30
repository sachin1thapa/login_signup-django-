from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='name'),
    path('signup' , views.signup , name='signup'),
    path('login' , views.login , name='login'),
    path('data' , views.sign , name='data')
]