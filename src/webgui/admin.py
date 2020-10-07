from django.contrib import admin
from .models import Event, TimeSlot, Booking
# Register your models here.

admin.site.register(Event)
admin.site.register(TimeSlot)
admin.site.register(Booking)
