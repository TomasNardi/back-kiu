# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = 'kiu-test'
copyright = '2025, tomas nardi'
author = 'tomas nardi'
release = '0.1'

# -- Path setup --------------------------------------------------------------
import os
import sys
from pathlib import Path

# Añadir la carpeta backend al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(Path(__file__).resolve().parents[2], 'backend')))

# Inicializar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  # Ajusta según tu settings.py
import django
django.setup()

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',     
    'sphinx.ext.napoleon',   
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']
