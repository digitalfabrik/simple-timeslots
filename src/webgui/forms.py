from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['timeslot', 'contact_name', 'contact_mail', 'contact_phone']
        labels = {'timeslot': 'Uhrzeit',
                  'contact_name': 'Ihr Name / Your Name / اسمك',
                  'contact_mail': "E-Mail / e-mail / البريد الإلكتروني",
                  'contact_phone': "Telefonnummer / phone number / رقم الهاتف"
                }

