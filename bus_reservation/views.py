from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Reservation
from .serializers import ReservationSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

# 메인 페이지 렌더링
def main(request):
    return render(request, 'bus_reservation/main.html')

# 동적 HTML 파일 렌더링
def render_template(request, filename):
    return render(request, f'bus_reservation/{filename}.html')

# 예약 생성 API
@csrf_exempt
@api_view(['POST'])
def create_reservation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 모든 예약 조회 API
@api_view(['GET'])
def get_reservations(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

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