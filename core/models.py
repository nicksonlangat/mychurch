from django.db import models
import datetime
from django.utils import timezone
from accounts.models import User

# Create your models here.

SERVICE_TYPE_CHOICES = [
        ('First Service', 'First Service'),
        ('Second Service', 'Second Service'),
        ('Third Service', 'Third Service'),
        ('Youngsters Service', 'Youngsters Service'),
        ('Midweek Service', 'Midweek Service'),
    ]
SEAT_STATUS_CHOICES = (
    (1, 'Available'),
    (2, 'Blocked'),
    (3, 'Booked')
)
class Service(models.Model):
	name=models.CharField(max_length=20)
	service_type = models.CharField(max_length=20,choices=SERVICE_TYPE_CHOICES)
	date=models.DateField()
	seat_capacity=models.PositiveIntegerField()
	live = models.BooleanField(default=True)

	def __str__(self):
		return f'{self.name} on {self.date}'

class Seat(models.Model):
	number=models.PositiveIntegerField()
	is_reserved = models.BooleanField(default=False)

	def __str__(self):
		return str(self.number)

class Attendance(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	service=models.ForeignKey(Service, on_delete=models.CASCADE, related_name='attended_service')
	seat=models.ForeignKey(Seat, on_delete=models.CASCADE)
	check_in = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.user} attended {self.service} and booked seat number {self.seat}'

