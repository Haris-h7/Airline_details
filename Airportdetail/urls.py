from django.urls import path
from Airportdetail import views




urlpatterns=[path("",views.index,name="index"),]