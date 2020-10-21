"""
All required models
"""
from django.db import models

class Event(models.Model):
    title = models.CharField("Titel", max_length=255)
    date = models.DateField("Datum", auto_now=False)
    location = models.CharField("Ort", max_length=512)
    location_link = models.URLField("Karten-Link", max_length=255, blank=True)
    description = models.TextField("Beschreibung", blank=True)
    manager_mail = models.EmailField("E-Mail", blank=True)

    def __str__(self):
        return self.title + " - " + self.location

    class Meta:
        verbose_name = "Veranstaltung"
        verbose_name_plural = "Veranstaltungen"

class TimeSlot(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="timeslots")
    start = models.TimeField("Start", auto_now=False)
    end = models.TimeField("Ende", auto_now=False)

    def __str__(self):
        return str(self.start) + " - " + str(self.end)

    class Meta:
        verbose_name = "Zeitslot"
        verbose_name_plural = "Zeitslots"

class Booking(models.Model):
    timeslot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE, related_name="booking")
    contact_name = models.CharField("Name", max_length=255, blank=True)
    contact_mail = models.EmailField("E-Mail Adresse", blank=True)
    contact_phone = models.CharField("Telefonnummer", max_length=255, blank=True)
    token = models.CharField("Token", max_length=16, blank=True)

    def __str__(self):
        return self.timeslot.event.title + " " + str(self.timeslot.event.date) + " " + str(self.timeslot.start) + " - Name: " + self.contact_name + ", Mail: " + self.contact_mail + ", Telefon: " + self.contact_phone

    class Meta:
        verbose_name = "Buchung"
        verbose_name_plural = "Buchungen"
