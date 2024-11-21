from django.contrib import admin
from django.urls import path
from bus_reservation import views
from . import views

app_name='reservation'

urlpatterns = [
    path('', views.main, name='main'),  
    path('<str:filename>.html', views.render_template, name='render_template'),  # 동적 URL 처리
    
    # API 경로
    # 예약 저장 (POST)
    path('api/reservation/', views.save_reservation, name='save_reservation'),
    # 모든 예약 조회 (GET)
    path('api/reservations/', views.get_reservations, name='get_reservations'),    
    # 특정 예약 상세 조회 (GET)
    path('api/reservation/<uuid:id>/', views.reservation_details, name='reservation_details'),
]
