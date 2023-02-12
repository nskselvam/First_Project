from django.urls import path
from . import views
app_name='room'
urlpatterns=[
    path('<int:lst_int>',views.details,name='details'),
    path('',views.index,name='index'),
]