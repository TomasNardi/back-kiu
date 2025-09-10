KIU / Tomas Nardi Documentation
================================

Created by **Tomas Nardi** for the technical entry test for the company KIU - Junior Level.

Project Description
===================

**Flight Search Endpoint for Passengers**

This project consists of the development of a **simple REST API** that allows **searching for direct flights** using a **static JSON database**. The API is designed to be:

- **Simple and easy to understand.**
- **Modular**, with a single endpoint.

Objective
=========

The main objective is to demonstrate basic knowledge of **Python**, **Django**, and **REST API**, creating a functional flight search system.

Project Structure
=================

- `backend/` → Django project configuration.
- `backend/kiu_flights/` → Main application handling the flight search logic.
- `kiu_flights/flight_data/flight.json` → Static database with the flights.
- `requirements.txt` → Dependencies required to run the project.
- `README.md` → Description and usage guide.

API Endpoints
=============

- **`/journeys/search/`**: Main endpoint to search for flights.  
  Accepts parameters such as `origin`, `destination`, and `date`, and returns a list of matching flights.

JSON Response Example
--------------------

.. code-block:: json

  {
    "flight_number": "AR1001",
    "from": "BUE",
    "to": "MAD",
    "departure_time": "2024-12-15 10:00",
    "arrival_time": "2024-12-15 23:00"
  }

Detailed Documentation
======================

For more details and descriptions of each endpoint, navigate to the following link:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   example
   endpoint
