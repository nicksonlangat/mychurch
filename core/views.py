from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView
from .models import *
from .forms import *

# Create your views here.
class AttendanceCreate(LoginRequiredMixin, CreateView):
    model = Attendance
    fields = ['service', 'seat']
    template_name="new_attendance.html"

    def form_valid(self, form):   #the current logged in user will automatically be added as the doc author 
        form.instance.user = self.request.user
        return super().form_valid(form)

class AttendanceList(LoginRequiredMixin, ListView):
    model = Attendance
    template_name="list.html"

class ServiceList(LoginRequiredMixin, ListView):
    model = Service
    template_name="service_list.html"

class SeatList(LoginRequiredMixin, ListView):
    model = Seat
    template_name="seat_list.html"
