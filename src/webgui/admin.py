from django.contrib import admin
from .models import Event, TimeSlot, Booking
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('timeslot__event',)

admin.site.register(Event)
admin.site.register(TimeSlot)
