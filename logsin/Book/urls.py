from django.urls import path
from . import views

urlpatterns =[
    path('' , views.library , name='bookhome'),
    path('libform',views.my_view , name='libform'),
    path('libdata',views.libdata , name='libdata'),
]