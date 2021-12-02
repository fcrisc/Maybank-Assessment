from django.http.response import JsonResponse
from django.shortcuts import render
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz
from .forms import DateTimeForm


import requests

# Create your views here.

def apiOverview(request):
    response = requests.get('http://api.open-notify.org/iss-now.json')
    tz = pytz.timezone("Asia/Kuala_Lumpur")
    issdata = response.json()
    
    iss_datetime = datetime.fromtimestamp(issdata['timestamp'], tz)
    geolocator = Nominatim(user_agent="geoapiExercises")
    latitude = str(issdata['iss_position']['latitude'])
    longitude = str(issdata['iss_position']['longitude'])
    
    location = geolocator.reverse(latitude+","+longitude)
    
    context = {
        'iss_datetime': iss_datetime,
        'latitude': latitude,
        'longitude': longitude,
        'location': location,
        }
    
    context['form'] = DateTimeForm()
    
    if request.POST:
        temp = request.POST['dateTime_input']
        print(type(temp))
    
    return render(request, 'api/iss-location.html', context)
