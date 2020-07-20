from django.urls import path
from .views import *
urlpatterns = [
    path('', ServiceList.as_view(),name="home"),
    path('book-a-seat', AttendanceCreate.as_view(),name="book"),
    path('attendances', AttendanceList.as_view(),name="attendances"),
    path('seats', SeatList.as_view(),name="seats"),
]