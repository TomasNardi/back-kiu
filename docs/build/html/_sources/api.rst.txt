Example Request
---------------

.. code-block:: bash

   curl -X GET "http://127.0.0.1:8000/journeys/search/?origin=BUE&destination=MAD&date=2024-12-15"

Example Response
----------------

.. code-block:: json

   {
     "flight_number": "AR1001",
     "from": "BUE",
     "to": "MAD",
     "departure_time": "2024-12-15 10:00",
     "arrival_time": "2024-12-15 23:00"
   }
