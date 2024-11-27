from django.contrib import admin
from .models import Reservation
from bus_reservation.models import Reservation
from bus_reservation.models import BusSchedule
from django.apps import apps

admin.site.register(Reservation)
Reservation = apps.get_model('bus_reservation','Reservation')

admin.site.register(BusSchedule)
BusSchedule = apps.get_model('bus_reservation','BusSchedule')