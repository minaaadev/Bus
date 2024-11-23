from django.shortcuts import render
from .serializers import ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reservation
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# 메인 페이지 렌더링
def main(request):
    return render(request, 'bus_reservation/main.html')


# 동적 HTML 파일 렌더링
def render_template(request, filename):
    # templates/bus_reservation/ 경로에 있는 HTML 파일 렌더링
    return render(request, f'bus_reservation/{filename}.html')


#CSRF TEST
@csrf_exempt
def save_reservation(request):
    if request.method == 'POST':
        # JSON 데이터 읽기
        import json
        data = json.loads(request.body)
        print(data)  # 디버깅용
        # 요청 데이터 처리 로직 추가
        return JsonResponse({'message': '예약이 완료되었습니다!'})
    return JsonResponse({'error': '허용되지 않은 요청입니다.'}, status=403)


# 모든 예약 조회 API
@api_view(['GET'])
def get_reservations(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
def create_reservation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def reservation_detail(request, pk):
    try:
        reservation=Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializr = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# # 특정 예약 상세 조회 API
# @api_view(['GET'])
# def reservation_details(request, id):
#     try:
#         reservation = Reservation.objects.get(id=id)

#         # 예약 데이터를 Response 객체로 반환
#         data = {
#             'id': str(reservation.id),
#             'departure': reservation.departure,
#             'arrival': reservation.arrival,
#             'date': reservation.date.strftime('%Y-%m-%d'),
#             'departureTime': reservation.departureTime.strftime('%H:%M'),
#             'arrivalTime': reservation.arrivalTime.strftime('%H:%M'),
#             'seatNumber': reservation.seatNumber,
#             'grade': reservation.grade
#         }
#         return Response({'reservation': data}, status=200)  # Response로 반환

#     except Reservation.DoesNotExist:
#         return Response({'error': 'Reservation not found'}, status=404)