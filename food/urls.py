from . import views
from django.urls import path
app_name='food'
urlpatterns = [
    path('', views.index,name='index'),
    path('first/',views.first,name='first'),
    # path('details/',views.details,name='details'),
    path('<int:listing_id>', views.details, name='details'),
    path('add/',views.Adddata,name='Adddata'),
]