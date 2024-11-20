from django.contrib import admin
from .models import Reservation
#임포트 경로 명시적 작성
from bus_reservation.models import Reservation
from django.apps import apps

admin.site.register(Reservation)
Reservation = apps.get_model('bus_reservation','Reservation')