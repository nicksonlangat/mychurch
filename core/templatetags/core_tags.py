from django import template
from django.db.models import Count
from ..models import *

register=template.Library()

@register.simple_tag
def total_attendances():
	return Attendance.published.count()

@register.simple_tag
def rem_attendances():
	x=100 - total_attendances()
	return x