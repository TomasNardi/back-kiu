from django.urls import path
from . import views

urlpatterns = [
    # Endpoint for searching flights
    path('journeys/search/', views.search_flights, name='search_flight'),
]