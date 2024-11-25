from django.contrib import admin
from django.urls import path
from bus_reservation import views
from .views import ReservationDetailAPIView


app_name = 'reservation'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('<str:filename>.html', views.render_template, name='render_template'),

    # API 경로
    path('reservation/create/', views.create_reservation, name='create_reservation'),
    path('reservations/', views.get_reservations, name='get_reservations'),
    path('reservation/<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('api/reservation/<int:pk>/', ReservationDetailAPIView.as_view(), name='reservation-detail'),

]
