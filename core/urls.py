from django.urls import path
from .views import *
from . import views
urlpatterns = [ 
    path('',views.attendance,name="home"),
    path('attendances', AttendanceList.as_view(),name="attendances"),
    # path('', AttendanceCreate.as_view(),name="home"),
    # path('list',views.services,name="list"),
    # path('seats', SeatList.as_view(),name="seats"),
]