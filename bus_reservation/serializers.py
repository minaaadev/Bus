from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'departure', 'arrival', 'date', 'departureTime', 'arrivalTime', 'seatNumber', 'grade']