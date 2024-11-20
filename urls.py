from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지
    path('', include('bus_reservation.urls')),  # bus_reservation 앱의 URL을 포함
]