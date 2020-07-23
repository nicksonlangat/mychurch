from django.db import models
import datetime
from django.utils import timezone
from accounts.models import User
from django.urls import reverse

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

STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

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
	first_name=models.CharField(max_length=20)
	middle_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	phone_number=models.PositiveIntegerField(unique=True)
	email=models.CharField(max_length=20, blank=True, null=True)
	service=models.ForeignKey(Service, on_delete=models.CASCADE, related_name='attended_service')
	seat=models.ForeignKey(Seat, on_delete=models.CASCADE)
	# check_in = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='published')
	objects = models.Manager()
	published = PublishedManager()

	def __str__(self):
		return f'{self.first_name} attended {self.service.name} and booked seat number {self.seat}'

	# def get_absolute_url(self):
	# 	return reverse('attendances')
        

