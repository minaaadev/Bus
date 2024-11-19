from django.shortcuts import render

def home(request):
    return render(request, 'bus_reservation/index.html')