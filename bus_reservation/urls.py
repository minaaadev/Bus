"""
URL configuration for bus_reservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bus_reservation import views
from . import views
# 개복치강의 from bus_reservation.api import ReservationList

app_name='reservation'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),  
    path('<str:filename>.html', views.render_template, name='render_template'),  # 동적 URL 처리
    path('save/', views.save_reservation, name='save_reservation'),
    path('details/<str:id>/', views.reservation_details, name='details'),
    # 개복치강의 path('api/reservation_list', ReservationList.as_view(), name='reservation_list')
]



