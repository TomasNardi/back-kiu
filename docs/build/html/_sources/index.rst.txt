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
- `kiu_flights/views.py` → Search Flight view function.
- `kiu_flights/urls.py` → API endpoints.
- `backend/kiu_flights/` → Main application handling the flight search logic.
- `kiu_flights/flight_data/flight.json` → Static database containing flight information.
- `requirements.txt` → Project dependencies.
- `README.md` → Project description and usage guide.

API Endpoints
=============

- **`/journeys/search/`**: Main endpoint to search for flights.  
  Accepts parameters such as `origin`, `destination`, and `date`, and returns a list of matching flights.

Please Read the Install Documentation
--------------------------------------

For detailed instructions, you can view the full documentation here:

.. note::

   Open the documentation in your browser: `KIU / Tomas Nardi Documentation <installation.html>`_


Detailed Documentation
======================

For more details and descriptions of each endpoint, navigate to the following link:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   example
   endpoint
   testing
