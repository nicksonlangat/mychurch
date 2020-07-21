from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView
from .models import *
from .forms import *

# Create your views here.
class AttendanceCreate(CreateView):
    model = Attendance
    fields = ['first_name','middle_name','last_name','phone_number','email','service','seat']
    template_name="new_attendance.html"

class AttendanceList(ListView):
    model = Attendance
    template_name="list.html"

class ServiceList(LoginRequiredMixin, ListView):
    model = Service
    template_name="service_list.html"

class SeatList(LoginRequiredMixin, ListView):
    model = Seat
    template_name="seat_list.html"
