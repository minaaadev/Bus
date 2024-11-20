import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from bus_reservation.models import Reservation
from django.views.decorators.csrf import csrf_exempt

def main(request):
    return render(request, 'bus_reservation/main.html')

def render_template(request, filename):
    # templates/bus_reservation/ 경로에 있는 HTML 파일 렌더링
    return render(request, f'bus_reservation/{filename}.html')


@csrf_exempt  # CSRF 토큰 비활성화 (개발 단계에서만 사용)
def save_reservation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # JSON 데이터를 파싱
            reservation = Reservation.objects.create(
                departure=data['departure'],
                arrival=data['arrival'],
                date=data['date'],
                departureTime=data['departureTime'],
                arrivalTime=data['arrivalTime'],
                seatNumber=data['seatNumbers'],
                grade=data['grade']
            )
            return JsonResponse({'id': str(reservation.id)}, status=201)  # 성공 시 예약 ID 반환
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)  # 오류 발생 시 메시지 반환
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def reservation_details(request, id):
    try:
        reservation = Reservation.objects.get(id=id)
        context = {
            'reservation': {
                'id': str(reservation.id),
                'departure': reservation.departure,
                'arrival': reservation.arrival,
                'date': reservation.date.strftime('%Y-%m-%d'),
                'departureTime': reservation.departureTime.strftime('%H:%M'),
                'arrivalTime': reservation.arrivalTime.strftime('%H:%M'),
                'seatNumber': reservation.seatNumber,
                'grade': reservation.grade
            }
        }
        return render(request, 'bus_reservation/reservation_details.html', context)
    except Reservation.DoesNotExist:
        return JsonResponse({'error': 'Reservation not found'}, status=404)