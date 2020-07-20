from django.db import models
from accounts.models import User

# Create your models here.

SERVICE_TYPE_CHOICES = [
        ('First Service', 'First Service'),
        ('Second Service', 'Second Service'),
        ('Third Service', 'Third Service'),
        ('Youngsters Service', 'Youngsters Service'),
        ('Midweek Service', 'Midweek Service'),
    ]
class Service(models.Model):
	name=models.CharField(max_length=20)
	service_type = models.CharField(max_length=20,choices=SERVICE_TYPE_CHOICES)
	date=models.DateField()
	seat_capacity=models.PositiveIntegerField()

	def __str__(self):
		return f'{self.name} on {self.date}'

class Seat(models.Model):
	number=models.PositiveIntegerField()

	def __str__(self):
		return str(self.number)

class Attendance(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	service=models.ForeignKey(Service, on_delete=models.CASCADE, related_name='attended_service')
	seat=models.ForeignKey(Seat, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user} attended {self.service} and booked seat number {self.seat}'

