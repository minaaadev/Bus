#내가한거
#import json
from django.shortcuts import render
from .serializers import ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reservation
from django.views.decorators.csrf import csrf_exempt


# 메인 페이지 렌더링
def main(request):
    return render(request, 'bus_reservation/main.html')


# 동적 HTML 파일 렌더링
def render_template(request, filename):
    # templates/bus_reservation/ 경로에 있는 HTML 파일 렌더링
    return render(request, f'bus_reservation/{filename}.html')


# 예약 저장 API
@csrf_exempt
@api_view(['POST'])
def save_reservation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': '예약이 완료되었습니다!', 'data': serializer.data}, status=201)
    return Response(serializer.errors, status=400)


# 모든 예약 조회 API
@api_view(['GET'])
def get_reservations(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data, status=200)


# 특정 예약 상세 조회 API
@api_view(['GET'])
def reservation_details(request, id):
    try:
        reservation = Reservation.objects.get(id=id)

        # 예약 데이터를 Response 객체로 반환
        data = {
            'id': str(reservation.id),
            'departure': reservation.departure,
            'arrival': reservation.arrival,
            'date': reservation.date.strftime('%Y-%m-%d'),
            'departureTime': reservation.departureTime.strftime('%H:%M'),
            'arrivalTime': reservation.arrivalTime.strftime('%H:%M'),
            'seatNumber': reservation.seatNumber,
            'grade': reservation.grade
        }
        return Response({'reservation': data}, status=200)  # Response로 반환

    except Reservation.DoesNotExist:
        return Response({'error': 'Reservation not found'}, status=404)
# def save_reservation(request):
#     if request.method == "POST":
#         try:
#             # JSON 데이터 읽기
#             data = json.loads(request.body) 
#             # 파일 경로 지정 (프로젝트 디렉토리 안에 reservations.json 생성)
#             file_path = os.path.join(os.path.dirname(__file__), "reservations.json")
            
#             # 데이터 저장 (추가 모드)
#             with open(file_path, "a") as file:
#                 json.dump(data, file)
#                 file.write("\n")  # 줄바꿈 추가
            
#             return JsonResponse({"message": "예약 정보가 성공적으로 저장되었습니다!"}, status=200)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
    
#     return JsonResponse({"error": "Invalid request method"}, status=400)


# @csrf_exempt  # CSRF 토큰 비활성화 (개발 단계에서만 사용)
# def save_reservation(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)  # JSON 데이터 읽어들임
            
#             reservation = Reservation.objects.create(
#                 departure=data['departure'],
#                 arrival=data['arrival'],
#                 date=data['date'],
#                 departureTime=data['departureTime'],
#                 arrivalTime=data['arrivalTime'],
#                 seatNumber=data['selectedSeats'], #수정
#                 grade=data['grade']
#             )
#             return JsonResponse({'id': str(reservation.id),'message': '예약이 완료되었습니다'},status=201)  # 성공 시 예약 ID 반환
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)  # 오류 발생 시 메시지 반환
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


# def reservation_details(request, id):
#     try:
#         reservation = Reservation.objects.get(id=id)

#         # 예약 데이터를 JSON 형식으로 반환
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
#         return JsonResponse({'reservation': data}, status=200)   
#     except Reservation.DoesNotExist:
#         return JsonResponse({'error': 'Reservation not found'}, status=404)