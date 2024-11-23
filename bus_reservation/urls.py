from django.contrib import admin
from django.urls import path
from bus_reservation import views
from .views import create_reservation, get_reservations,reservation_detail

app_name='reservation'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.main, name='main'),  
    path('<str:filename>.html', views.render_template, name='render_template'),  # 동적 URL 처리
    
    # API 경로
    # 예약 저장 (POST)
    path('reservation/create/', create_reservation, name='create_reservation'),
    
    # 모든 예약 조회 (GET)
    path('reservations/', get_reservations, name='get_reservations'),    
    # 특정 예약 상세 조회 (GET)
    path('reservation/<int:pk>/', reservation_detail, name='reservation_detail'),
]