from django.forms import ModelForm
from .models import *

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'