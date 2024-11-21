from rest_framework import serializers
from .models import Reservation
#db와 api response 연동

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'departure', 'arrival', 'date', 'departureTime', 'arrivalTime', 'seatNumber', 'grade']