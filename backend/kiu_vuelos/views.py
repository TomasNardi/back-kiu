# views.py
from rest_framework.decorators import api_view
from django.conf import settings
import os

# JSON file path - always use relative paths, avoid absolute paths in production
FLIGHTS_JSON_PATH = os.path.join(settings.BASE_DIR, 'kiu_vuelos', 'flight_data', 'flight.json')

@api_view(['GET'])
def search_flights(request):
    # Get query parameters
    date_param = request.GET.get('date')
    from_param = request.GET.get('from')
    to_param = request.GET.get('to')
    
    # Print the received parameters for debugging
    print(f"[DEBUG] Received parameters -> date: {date_param}, from: {from_param}, to: {to_param}")
