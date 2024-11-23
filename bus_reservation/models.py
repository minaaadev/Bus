from django.db import models 
import uuid

class Reservation(models.Model) :
    #예약시 랜덤으로 id 부여 
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    departure = models.CharField(max_length=10)
    arrival = models.CharField(max_length=10)

    date = models.DateField(auto_now_add=True)
    departureTime = models.TimeField()
    arrivalTime = models.TimeField()

    seatNumber = models.CharField(max_length=10)
    grade = models.CharField(max_length=10)

    created_at=models.DateTimeField(auto_now_add=True) #예약 생성 시간 

    def __str__(self):
        return f"{self.id} 의 예약이 완료되었습니다."