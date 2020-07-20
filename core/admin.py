from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Seat)
admin.site.register(Service)
admin.site.register(Attendance)
admin.site.site_header = 'GOSPEL REVIVAL WAVE CHURCH'        
admin.site.index_title = 'GRWC AREA'
admin.site.site_title = 'GRWC ADMIN'