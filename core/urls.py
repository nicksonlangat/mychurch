from django.urls import path
from .views import *
urlpatterns = [
    path('list', ServiceList.as_view(),name="list"),
    path('', AttendanceCreate.as_view(),name="home"),
    path('attendances', AttendanceList.as_view(),name="attendances"),
    path('seats', SeatList.as_view(),name="seats"),
]