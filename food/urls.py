from . import views
from django.urls import path
urlpatterns = [
    path('', views.index,name='index'),
    path('first/',views.first,name='first'),
    # path('details/',views.details,name='details'),
    path('<int:listing_id>', views.details, name='details'),
]