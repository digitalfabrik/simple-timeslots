# Generated by Django 3.1.2 on 2020-10-07 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titel')),
                ('date', models.DateField(verbose_name='Datum')),
                ('location', models.CharField(max_length=512, verbose_name='Ort')),
                ('location_link', models.URLField(blank=True, max_length=255, verbose_name='Karten-Link')),
                ('description', models.TextField(blank=True, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Veranstaltung',
                'verbose_name_plural': 'Veranstaltungen',
            },
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField(verbose_name='Start')),
                ('end', models.TimeField(verbose_name='Ende')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeslots', to='webgui.event')),
            ],
            options={
                'verbose_name': 'Zeitslot',
                'verbose_name_plural': 'Zeitslots',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('contact_mail', models.EmailField(blank=True, max_length=254, verbose_name='E-Mail Adresse')),
                ('contact_phone', models.CharField(blank=True, max_length=255, verbose_name='Telefonnummer')),
                ('timeslot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='webgui.timeslot')),
            ],
        ),
    ]