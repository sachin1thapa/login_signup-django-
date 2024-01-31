from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='name'),
    path('signup' , views.signup , name='signup'),
    path('login' , views.loginform , name='login'),
    path('signupdata' , views.signupdata , name='signupdata'),
    path('logindata' , views.logindata , name='logindata'),
    path('msg' , views.msg , name = 'msg')
    
]