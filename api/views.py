from django.http.response import JsonResponse
from django.shortcuts import render
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import pytz
from .forms import DateTimeForm
from datetime import datetime


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
        date = request.POST['date']
        time = request.POST['time']
        datetime_combine = str(date + " " + time)
        datetime_format = datetime.strptime(datetime_combine, '%Y-%m-%d %H:%M')
        timestamp_value = datetime.timestamp(datetime_format)
        # print(timestamp_value)
        datetime_after = []
        for i in range(5):
            cal_datetime = datetime_format + timedelta(minutes = 10)
            datetime_after.append(cal_datetime)
            timestamp_after = datetime.timestamp(datetime_format)
            
        api_url = 'https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps='+str(timestamp_value)
            
        response_details = requests.get(api_url)
        issdata_details = response_details.json()
        
        print(issdata_details)
        
        iss_datetime_details = datetime.fromtimestamp(issdata_details[0]['timestamp'], tz)
        geolocator_details = Nominatim(user_agent="geoapiExercises")
        latitude_details = str(issdata_details[0]['latitude'])
        longitude_details = str(issdata_details[0]['longitude'])
        
        location_details = geolocator_details.reverse(latitude_details+","+longitude_details)
        
        context['iss_datetime_details'] = iss_datetime_details
        context['latitude_details'] = latitude_details
        context['longitude_details'] = longitude_details
        context['location_details'] = location_details
        
        print(api_url)
        
    return render(request, 'api/iss-location.html', context)
