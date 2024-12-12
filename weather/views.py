from django.shortcuts import render

def dashboard(request):
    return render(request, 'weather/weather_dashboard.html')
