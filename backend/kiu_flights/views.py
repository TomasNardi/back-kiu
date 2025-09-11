# views.py
import json
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import os
from django.http import JsonResponse

def keep_alive(request):
    """
    Simple endpoint to keep the server alive.
    """
    return JsonResponse({"status": "alive"}, status=200)

# JSON file path - always use relative paths, avoid absolute paths in production
FLIGHTS_JSON_PATH = os.path.join(settings.BASE_DIR, 'kiu_flights', 'flight_data', 'flight.json')

@api_view(['GET'])
def search_flights(request):
    """
    Search for flights based on departure date, origin, and destination.

    This function is divided into two main parts:

    1. Input validation (pre-filter):
       - Ensures that all required query parameters (`date`, `from`, `to`) are provided.
       - Checks that city codes are exactly 3 uppercase letters.
       - Validates that the date is in the 'YYYY-MM-DD' format.
       - Returns a 400 error if any validation fails.

    2. Flight search (data filter):
       - Loads flight data from a JSON file.
       - Iterates through all flights and selects those that match:
         * `from_city` == departure_city
         * `to_city` == arrival_city
         * `date_str` matches the departure date
       - Returns a list of matching flights with relevant information.
       - Returns an empty list if no flights are found.

    Args:
        request (Request): A DRF Request object containing GET parameters:
            - `date` (str): Departure date in 'YYYY-MM-DD' format.
            - `from` (str): 3-letter uppercase code of the origin city.
            - `to` (str): 3-letter uppercase code of the destination city.

    Returns:
        Response:
            - 400 error with message if input is invalid.
            - A list of matching flights with keys: `flight_number`, `from`, `to`, 
              `departure_time`, `arrival_time`.
    """
    
    # Get query parameters
    date_str = request.GET.get('date')
    from_city = request.GET.get('from')
    to_city = request.GET.get('to')

    # 1 (Objetive). Parámetros obligatorios: Los 3 parámetros (date, from, to) deben estar presentes 
    # Basic validations (case of empty fields) - 400 Error.
    if not date_str or not from_city or not to_city:
        return Response({"error": "Los parámetros (date, from y to) son obligatorios."}, status=status.HTTP_400_BAD_REQUEST)
    
    # 3 (Objetive). Códigos de ciudad: Deben ser exactamente 3 letras mayúsculas.
    # Case from-to City lenght is not 3 or is not Upper Case.
    if len(from_city) != 3 or len(to_city) != 3 or not from_city.isupper() or not to_city.isupper():
        return Response({"error": "Los códigos de ciudad deben ser 3 letras mayúsculas."}, status=status.HTTP_400_BAD_REQUEST)
    
    # 2 (Objetive). Formato de fecha: Debe ser YYYY-MM-DD
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return Response({"error": "El formato de fecha debe ser YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

    # Load the Json Document.
    with open(FLIGHTS_JSON_PATH, 'r') as f:
        flights = json.load(f)

    # 4 (Objetive). Filtrado: Solo mostrar vuelos que coincidan exactamente con los parámetros , sino devolver [].
    # Results after searching flight.json! 
    
    results = []
    for flight in flights:
    # Check for a full match between the flight data and the query parameters.
    # Note:
    #   - Use `append` because there could be more than one flight
    #     that matches the same origin, destination, and date.
        if (flight['departure_city'] == from_city and
            flight['arrival_city'] == to_city and
            flight['departure_datetime'].startswith(date_str)):
            
            results.append({
                "flight_number": flight['flight_number'],
                "from": flight['departure_city'],
                "to": flight['arrival_city'],
                "departure_time": flight['departure_datetime'][:16].replace("T", " "),
                "arrival_time": flight['arrival_datetime'][:16].replace("T", " ")
            })


    return Response(results)
