from django.shortcuts import render
from .serializers import ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reservation
from .models import BusSchedule  # BusSchedule 모델 임포트
from rest_framework import status
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404



# 메인 페이지 렌더링
def main(request):
    return render(request, 'bus_reservation/main.html')


# 동적 HTML 파일 렌더링
def render_template(request, filename):
    # templates/bus_reservation/ 경로에 있는 HTML 파일 렌더링
    return render(request, f'bus_reservation/{filename}.html')

def check_schedule(request):
    # 출발지와 도착지, 날짜를 GET 파라미터로부터 가져오기
    departure = request.GET.get('departure')
    arrival = request.GET.get('arrival')
    date = request.GET.get('date')

    # 출발지와 도착지에 맞는 모든 버스 시간표 조회
    bus_schedules = BusSchedule.objects.filter(departure_city=departure, arrival_city=arrival)

    # 각 스케줄에 대해 잔여 좌석 계산
    for schedule in bus_schedules:
        # 관련된 모든 예약 가져오기
        reservations = Reservation.objects.filter(
            departure=schedule.departure_city,
            arrival=schedule.arrival_city,
            date=date,
            departureTime=schedule.departure_time
        )

        # 예약된 좌석 수 합산
        reserved_count = sum(len(reservation.seatNumber.split(',')) for reservation in reservations)

        # 잔여 좌석 계산
        schedule.seats_available = schedule.seats_available - reserved_count  # total_seats는 BusSchedule의 총 좌석 수

    context = {
        'departure': departure,
        'arrival': arrival,
        'date': date,
        'bus_schedules': bus_schedules,
    }

    return render(request, 'bus_reservation/check_schedule.html', context)



# 버스 좌석 예약 뷰 추가
def set_seat(request):
    # URL 매개변수 추출
    schedule_id = request.GET.get('schedule_id')
    departure = request.GET.get('departure')
    arrival = request.GET.get('arrival')
    date = request.GET.get('date')

    # BusSchedule 모델에서 해당 ID 조회
    try:
        schedule = BusSchedule.objects.get(id=schedule_id)
    except BusSchedule.DoesNotExist:
        return render(request, 'bus_reservation/error.html', {
            'message': '해당 스케줄을 찾을 수 없습니다.'
        })

    # 출발지와 도착지, 날짜, 출발시간에 맞는 예약 정보를 조회
    reservations_id = Reservation.objects.filter(
        departure=schedule.departure_city,
        arrival=schedule.arrival_city,
        date=date,
        departureTime=schedule.departure_time
    ).values_list("seatNumber", flat=True)

    # 항상 리스트로 변환
    reserved_seats = list(reservations_id) if reservations_id else []

    # 컨텍스트 데이터 준비
    context = {
        'schedule': schedule,
        'departure': departure,
        'arrival': arrival,
        'date': date,
        'reserved_seats': reserved_seats,  # 예약된 좌석 번호 리스트 전달
    }

    return render(request, 'bus_reservation/set_seat.html', context)



# 모든 예약 조회 API
@api_view(['GET'])
def get_reservations(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

# 예약 생성 API
@csrf_exempt
@api_view(['POST'])
def create_reservation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 특정 예약 조회, 수정, 삭제 API
@api_view(['GET', 'PUT', 'DELETE'])
def reservation_detail(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response({'error': 'Reservation not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reservation.delete()
        return Response({'message': 'Reservation deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    

#데이터를 JSON으로 반환
class ReservationDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            reservation = Reservation.objects.get(pk=pk)
            serializer = ReservationSerializer(reservation)
            return Response(serializer.data)
        except Reservation.DoesNotExist:
            return Response({"error": "Reservation not found"}, status=404)
        

# views.py
@api_view(['GET'])
def reservation_details(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)  # 확인: 데이터의 필드 이름이 무엇인지 점검
    except Reservation.DoesNotExist:
        return Response({'error': 'Reservation not found'}, status=404)
