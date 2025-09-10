KIU / Tomas Nardi Documentation
============================================

Creado por **Tomas Nardi** para la prueba técnica de ingreso a la compañía KIU - Nivel Junior.

Descripción del Proyecto
------------------------

**Desafío de Programación KIU – Nivel Junior**

Este proyecto consiste en el desarrollo de una **API REST simple** que permite **buscar vuelos directos** utilizando una **base de datos estática en formato JSON**. La API está diseñada para ser:

- **Sencilla y fácil de entender.**
- **Modular**, con un único endpoint.

Objetivo
--------

El objetivo principal es demostrar conocimientos básicos de **Python**, **Django**, y **REST API**, creando un sistema funcional de búsqueda de vuelos.

Estructura del Proyecto
----------------------

- `kiu_tomas_nardi/` → Configuración del proyecto Django.
- `kiu_flights/` → Aplicación principal que maneja la lógica de búsqueda de vuelos.
- `flight_data/flight.json` → Base de datos estática con los vuelos.
- `requirements.txt` → Dependencias necesarias para ejecutar el proyecto.
- `README.md` → Descripción y guía de uso.

Documentación de Endpoints
--------------------------

- **`/journeys/search/`**: Endpoint principal para buscar vuelos.  
  Recibe parámetros como `origin`, `destination` y `date`, y devuelve una lista de vuelos coincidentes.

json :
  {
    "flight_number": "AR1001",
    "from": "BUE",
    "to": "MAD",
    "departure_time": "2024-12-15 10:00",
    "arrival_time": "2024-12-15 23:00"
  }
