from django.shortcuts import render
from .utils import get_weather_data

def dashboard(request):
    # My location
    latitude = 59.3293
    longitude = 18.0686

    # Get weather data
    weather_data = get_weather_data(latitude, longitude)

    # If API returns no data
    if not weather_data:
        return render(request, 'weather/weather_dashboard.html', {"error": "Unable to fetch weather data."})

    # Extract data
    current_weather = weather_data.get("current_weather", {})
    daily_weather = weather_data.get("daily", {})

    context = {
        "current_weather": current_weather,
        "daily_weather": daily_weather,
    }
    return render(request, 'weather/weather_dashboard.html', context)
