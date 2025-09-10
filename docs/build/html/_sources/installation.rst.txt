Installation
============

To get started with the project and read the full documentation locally, follow these steps:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/TomasNardi/Kiu-tomas-nardi
      cd Kiu-tomas-nardi

2. Create and activate a virtual environment:

   .. code-block:: bash

      python -m venv .venv
      source .venv/bin/activate   # Linux/Mac
      .venv\Scripts\activate      # Windows

3. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Build the documentation:

   .. code-block:: bash

      cd docs
      make html        # Linux/Mac
      .\make.bat html  # Windows

5. Open the documentation in your browser:

   .. code-block:: text

      docs/build/html/index.html

   This will open the **project documentation** where you will find detailed instructions on:
   
   - Starting the server
   - Using the available API endpoints
   - Running tests
