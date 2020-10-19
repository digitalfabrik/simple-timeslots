import datetime
import secrets
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import BookingForm
from .models import Event, TimeSlot, Booking
# Create your views here.


def index(request):
    """
    List available events
    """
    now = datetime.datetime.now()
    events = Event.objects.filter(date__gte=now).order_by('date')
    context = {"events": events}
    return render(request, "index.html", context)

def event(request, event_id):
    """
    Display time slot form and event infos
    """
    token = None
    if request.method == "POST":
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            token = secrets.token_urlsafe(16)
            booking_form.instance.token = token
            booking_form.save()
            if booking_form.instance.contact_mail:
                send_mail('Termin gebucht / booked appointment / تم حجز الموعد',
                          ('Folgender Termin wurde gebucht / The following appointment was booked / تم حجز الموعد التالي:\n\n' +
                           str(booking_form.instance.timeslot.event.title) + '\n\n' +
                           str(booking_form.instance.timeslot.event.date) + ' ' + str(booking_form.instance.timeslot.start) +
                           '\n\n' + booking_form.instance.timeslot.event.location + '\n\n'
                           'Storno / Cancel / إلغاء: https://' + settings.DOMAIN + '/cancel/' + booking_form.instance.token) ,
                          settings.EMAIL_HOST_USER, [booking_form.instance.contact_mail], fail_silently=not(settings.DEBUG))
    event_info = Event.objects.get(id=int(event_id))
    booking_form = BookingForm()
    booking_form.fields['timeslot'].queryset = TimeSlot.objects.filter(event=event_info,booking__isnull=True)
    context = {"booking_form": booking_form, "event": event_info, "token": token, "domain": settings.DOMAIN}
    return render(request, "event.html", context)

def cancel(request, token):
    booking = Booking.objects.filter(token=token).first()
    if booking:
        time = booking.timeslot.start
        date = booking.timeslot.event.date
        send_mail('Buchung storniert', 'Buchung storniert für: ' + str(date) + ' ' + str(time), settings.EMAIL_HOST_USER, [booking.timeslot.event.manager_mail], fail_silently=not(settings.DEBUG))
        booking.delete()
        cancelled = True
    else:
        cancelled = False
        time = None
        date = None
    return render(request, "cancel.html", {"cancelled": cancelled, "time": time, "date": date})
