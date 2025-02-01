from django.contrib import admin
from django.urls import path
from bus_reservation import views
from .views import ReservationDetailAPIView
from . import views


app_name='reservation'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.main, name='main'),  
    path('<str:filename>.html', views.render_template, name='render_template'),  # 동적 URL 처리
    

    # 버스 시간표 조회 경로 추가
    path('check_schedule/', views.check_schedule, name='check_schedule'),

    path('set_seat.html/', views.set_seat, name='set_seat'),  # 추가

    # API 경로
    # 예약 저장 (POST)
    path('reservation/create/', views.create_reservation, name='create_reservation'),
    
    # 모든 예약 조회 (GET)
    path('reservations/', views.get_reservations, name='get_reservations'),    
    
    #데이터를 JSON으로 반환하는 API
    path('api/reservation/<int:pk>/', ReservationDetailAPIView.as_view(), name='reservation-detail')
]
