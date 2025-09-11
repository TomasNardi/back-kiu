from django.urls import path
from . import views

urlpatterns = [
    # Endpoint for searching flights
    path('journeys/search/', views.search_flights, name='search_flight'),
    # Keep-alive endpoint
    path('keep-alive/', views.keep_alive, name='keep_alive'),
]