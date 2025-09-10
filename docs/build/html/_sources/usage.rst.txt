Usage
=====

To use the Api and Testing :

1. **Be sure to read the Installation Guide:**

    `KIU Installation Section <installation.html>`_

2. **You must navigate to the backend directory and run:**

    # By default it should be on port 8000
      python manage.py runserver

3. **Then you can execute queries to the endpoint:**

   .. code-block:: bash

      curl -X GET "http://127.0.0.1:8000/journeys/search/?from=BUE&to=MAD&date=2024-12-15"

      It is recommended to read the Examples section.
