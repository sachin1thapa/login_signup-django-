from django.urls import path
from . import views

urlpatterns =[
    path('' , views.library , name='bookhome'),
    path('libform',views.my_view , name='libform'),
    path('libdata',views.libdata , name='libdata'),
    path('update_form/<int:book_id>/' , views.update_form , name='update_form'),
    path('remove/<int:remove_id>/',views.remove , name='remove'),
    path('search',views.search , name='search'),
]


