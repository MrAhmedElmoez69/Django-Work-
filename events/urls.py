from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage , name="Home_Page"),
    path('home/', homePage1 , name="Home_Page1"),
    path('listStatic/', listEventsStatic , name="Events_listS"),
    path('list/', listEvents , name="Events_list"),




]
