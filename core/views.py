from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView
from .models import *
from .forms import *
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponseForbidden,HttpResponse
from django.utils import timezone
# Create your views here.
def attendance(request):
    if request.method == "POST":
    	yesterday = timezone.now() - timezone.timedelta(days=1)
    	phone_number = request.POST['phone_number']
    	seat = request.POST['seat']
    	if Attendance.objects.filter(phone_number=phone_number, created__gt=yesterday).exists():
    		return render(request,'new_attendance.html',{"errors": "You have already booked a seat for this service, thank you."})
    	if Attendance.objects.filter(seat=seat).exists():
    		return render(request, 'new_attendance.html',{"errors": "The seat you selected has been booked, please try another."})
    	form = AttendanceForm(request.POST)
    	if form.is_valid():
    		form.save(commit=True)
    		return HttpResponseRedirect(reverse('thanks'))
    else:
        form = AttendanceForm()

    return render(request, 'new_attendance.html', {'form':form})

def thanks(request):
	return render(request,'thanks.html')

class AttendanceList(ListView):
    model = Attendance
    template_name="list.html"


# class AttendanceCreate(CreateView):
#     model = Attendance
#     fields = ['first_name','middle_name','last_name','phone_number','email','service','seat']
#     template_name="new_attendance.html"



# def services(request):
# 	services=Service.objects.all().filter(live=True)
# 	return render(request, 'service_list.html', {'services':services})

# class ServiceList(LoginRequiredMixin, ListView):
#     model = Service
#     template_name="service_list.html"

# class SeatList(LoginRequiredMixin, ListView):
#     model = Seat
#     template_name="seat_list.html"
