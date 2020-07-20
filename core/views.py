from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView
from .models import *
from .forms import *

# Create your views here.
class AttendanceCreate(LoginRequiredMixin, CreateView):
    model = Attendance
    fields = '__all__'
    template_name="new_attendance.html"

class AttendanceList(LoginRequiredMixin, ListView):
    model = Attendance
    template_name="attendance_list.html"

class ServiceList(LoginRequiredMixin, ListView):
    model = Service
    template_name="service_list.html"

class SeatList(LoginRequiredMixin, ListView):
    model = Seat
    template_name="seat_list.html"
