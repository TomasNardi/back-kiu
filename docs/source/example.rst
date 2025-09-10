Example
=======

Example Request
---------------

.. code-block:: bash

   # !Important! Make sure you have run `python manage.py runserver` and that it is running on port 8000

   curl -X GET "http://127.0.0.1:8000/journeys/search/?from=BUE&to=MAD&date=2024-12-15"

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
