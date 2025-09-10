# test.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import json
import os
from django.conf import settings

class SearchFlightsTestCase(APITestCase):
    """
    Test for the `search_flights` API endpoint.

    This class tests various scenarios for the flight search view:
    
    # 1 (Objetive). Parámetros obligatorios: Los 3 parámetros (date, from, to) deben estar presentes
    # 2 (Objetive). Formato de fecha: Debe ser YYYY-MM-DD
    # 3 (Objetive). Códigos de ciudad: Deben ser exactamente 3 letras mayúsculas.
    # 4 (Objetive). Filtrado: Solo mostrar vuelos que coincidan exactamente con los parámetros , sino devolver [].
 
    The tests use a temporary JSON file located in `flight_data/flight.json`. 
    
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for all test methods.

        Creates a temporary JSON file with sample flights:
        - NYC → LAX flight on 2025-09-15
        - NYC → SFO flight on 2025-09-15
        
        """
        cls.flight_data_path = os.path.join(settings.BASE_DIR, 'kiu_flights', 'flight_data', 'flight.json')
        os.makedirs(os.path.dirname(cls.flight_data_path), exist_ok=True)
        
        cls.test_flights = [
            {
                "flight_number": "AB123",
                "departure_city": "NYC",
                "arrival_city": "LAX",
                "departure_datetime": "2025-09-15T08:00",
                "arrival_datetime": "2025-09-15T11:00"
            },
            {
                "flight_number": "CD456",
                "departure_city": "NYC",
                "arrival_city": "SFO",
                "departure_datetime": "2025-09-15T09:00",
                "arrival_datetime": "2025-09-15T12:00"
            }
        ]
        with open(cls.flight_data_path, 'w') as f:
            json.dump(cls.test_flights, f)

    def test_missing_parameters(self):
        """
        Test that the endpoint returns 400 if any query parameter is missing.
        """
        url = reverse('search_flight')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.json())

    def test_invalid_city_code(self):
        """
        Test that the endpoint returns 400 if city codes are invalid
        (not 3 uppercase letters).
        """
        url = reverse('search_flight')
        response = self.client.get(url, {"date": "2025-09-15", "from": "NY", "to": "LAX"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.json())

    def test_invalid_date_format(self):
        """
        Test that the endpoint returns 400 if the date format is invalid
        (not YYYY-MM-DD).
        """
        url = reverse('search_flight')
        response = self.client.get(url, {"date": "15-09-2025", "from": "NYC", "to": "LAX"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.json())

    def test_no_flights_found(self):
        """
        Test that the endpoint returns 200 and an empty list
        if no flights match the query parameters.
        """
        url = reverse('search_flight')
        response = self.client.get(url, {"date": "2025-09-16", "from": "NYC", "to": "LAX"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])

    def test_flights_found(self):
        """
        Test that the endpoint returns 200 and a list of matching flights
        when flights match the query parameters.
        """
        url = reverse('search_flight')
        response = self.client.get(url, {"date": "2025-09-15", "from": "NYC", "to": "LAX"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["flight_number"], "AB123")
        self.assertEqual(data[0]["from"], "NYC")
        self.assertEqual(data[0]["to"], "LAX")
