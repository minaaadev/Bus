from django.db import models 
import uuid

class Reservation(models.Model) :
    #예약시 랜덤으로 id 부여 
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    departure = models.CharField(max_length=10)
    arrival = models.CharField(max_length=10)

    # auto_now_add=True 해제
    date = models.DateField()
    
    departureTime = models.TimeField()
    arrivalTime = models.TimeField()

    seatNumber = models.CharField(max_length=20)
    grade = models.CharField(max_length=10)

    created_at=models.DateTimeField(auto_now_add=True) #예약 생성 시간 

    def __str__(self):
        return f"{self.id} 의 예약이 완료되었습니다."
    

class BusSchedule(models.Model):
    
    departure_city = models.CharField(max_length=100)  # 출발지 도시
    arrival_city = models.CharField(max_length=100)    # 도착지 도시
    departure_time = models.TimeField()               # 출발 시간
    arrival_time = models.TimeField()                 # 도착 시간
    duration = models.CharField(max_length=50, default=None, null=True)         # 소요 시간 (문자열 형식)
    bus_class = models.CharField(max_length=50)       # 버스 등급 (예: 일반, 프리미엄 등)
    seats_available = models.PositiveIntegerField()   # 잔여 좌석 수

    class Meta:
        verbose_name = "Bus Schedule"
        verbose_name_plural = "Bus Schedules"
        ordering = ['departure_time']

    def __str__(self):
        return f"{self.departure_city} to {self.arrival_city} at {self.departure_time.strftime('%H:%M')}"
    

# 주요 요소:
# - departure_city: 출발지 도시
# - arrival_city: 도착지 도시
# - departure_time: 출발 시간
# - arrival_time: 도착 시간
# - bus_class: 버스 등급 (일반, 프리미엄 등등)
# - seats_available: 잔여 좌석 수

# 위 모델은 각 버스 시간표에 대한 정보를 저장하는 테이블을 정의합니다.
# 이를 통해 특정 일자와 경로에 맞는 버스 시간표를 데이터베이스에서 가져와 check_schedule.html 페이지에서 보여줄 수 있습니다.