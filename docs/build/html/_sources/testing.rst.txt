Testing API
===========

To use the testing section, you should be in the same directory as `manage.py` :

`Kiu-tomas-nardi\backend` → then run:

    python manage.py test kiu_flights.test_flights

In the PowerShell console, you should see a message like this:

.. code-block:: console

    Each dot represents a unit test
    .....

    Found 5 test(s).
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).

    Ran 5 tests in 0.670s

    OK
    Destroying test database for alias 'default'...

Also, if you want to see the full test cases, you should go to:

- `backend/kiu_flights/test_flights` → Testing Endpoint.

.. automodule:: kiu_flights.test_flights
    :members:
    :undoc-members:
    :show-inheritance:
